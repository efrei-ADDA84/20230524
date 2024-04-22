# Fournisseur
provider "azurerm" {
  skip_provider_registration = true
  features {}
}

# Variables
variable "subscription_id" {
  type    = string
  default = "765266c6-9a23-4638-af32-dd1e32613047"
}

variable "resource_group_name" {
  type    = string
  default = "ADDA84-CTP"
}

variable "location" {
  type    = string
  default = "francecentral"
}

variable "network_name" {
  type    = string
  default = "network-tp4"
}

variable "subnet_name" {
  type    = string
  default = "internal"
}

variable "vm_name" {
  type = string
  default = "20230524"
}

variable "admin_username" {
  type    = string
  default = "devops"
}

# Création de la clé SSH
resource "tls_private_key" "ssh_key" {
  algorithm = "RSA"
  rsa_bits  = 4096
}

# Definition d'un output pour la clé privé
output "private_key_pem" {
  value     = tls_private_key.ssh_key.private_key_pem
  sensitive = true
}

# Création de l'adresse IP publique
resource "azurerm_public_ip" "public_ip" {
  name                = "publicip"
  location            = var.location
  resource_group_name = var.resource_group_name
  allocation_method   = "Dynamic"
}

# Création de la machine virtuelle
resource "azurerm_linux_virtual_machine" "virtual_machine" {
  name                = "devops-${var.vm_name}"
  resource_group_name = var.resource_group_name
  location            = var.location
  size                = "Standard_D2s_v3"
  admin_username      = var.admin_username
  disable_password_authentication = true
  network_interface_ids = [azurerm_network_interface.nic.id]

  admin_ssh_key {
    username   = var.admin_username
    public_key = tls_private_key.ssh_key.public_key_openssh
  }

  os_disk {
    caching              = "ReadWrite"
    storage_account_type = "Premium_LRS"
  }

  source_image_reference {
    publisher = "Canonical"
    offer     = "0001-com-ubuntu-server-focal"
    sku       = "20_04-lts"
    version   = "latest"
}
}

# Récupération de l'ID du sous-réseau
data "azurerm_subnet" "subnet" {
  name                 = var.subnet_name
  virtual_network_name = var.network_name
  resource_group_name  = var.resource_group_name
}

# Création de l'interface réseau
resource "azurerm_network_interface" "nic" {
  name                = "nic-${var.vm_name}"
  location            = var.location
  resource_group_name = var.resource_group_name

  ip_configuration {
    name                          = "internal"
    subnet_id                     = data.azurerm_subnet.subnet.id
    private_ip_address_allocation = "Dynamic"
    public_ip_address_id          = azurerm_public_ip.public_ip.id
  }
}