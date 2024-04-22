# Rapport TP4

### Contexte

Dans ce TP, nous avons appris à créer et déployer une infrastructure cloud sur un fournisseur, ici Azure pour nous à travers la bibliothèque Terraform.
Terraform est un outil open source développé par HashiCorp qui permet de créer, modifier et gérer l'infrastructure informatique de manière déclarative et basée sur du code. Il fait partie de la catégorie des outils d'Infrastructure as Code (IaC).

### Technologie

Nous avons utilisé la bibliothèque Terraform pour orchestrer la création et le déploiement d'une infrastructure cloud sur Microsoft Azure, en nous appuyant sur un fichier de configuration nommé 'main.tf'. L'objectif principal était de gérer de manière efficiente la création et la configuration de cette infrastructure, en nous affranchissant des interfaces graphiques telles que Azure CLI ou l'interface utilisateur d'Azure. En outre, nous avons mis en place la génération automatique d'une clé SSH via Terraform afin de sécuriser l'accès à la machine virtuelle.

### Étapes

1. J'ai commencé par installer Terraform et Azure CLI à partir des packages disponibles sur les sites officiels respectifs.
2. Ensuite, j'ai créé le fichier de configuration de mon infrastructure cloud en me référant à la documentation et en spécifiant les paramètres requis dans le cadre du TP.
3. Une fois ma configuration prête, j'ai initialisé Terraform en exécutant la commande terraform init.
4. En utilisant la commande terraform apply, j'ai appliqué les changements pour créer et déployer mon infrastructure selon les spécifications que j'avais définies.
5. Avant de terminer, j'ai effectué un test de connexion à ma machine virtuelle via SSH en utilisant la commande ssh -i <clé_ssh> devops@<ADRESSE_IP> cat /etc/os-release. Cela m'a permis de vérifier la connectivité SSH et d'obtenir des informations sur le système d'exploitation de ma machine virtuelle.
   -> La clé privé a été stocké dans le fichier privateKey.pem
6. Enfin, une fois que j'ai confirmé que la connexion SSH fonctionnait correctement, j'ai procédé à la destruction de l'infrastructure en exécutant la commande terraform destroy, afin de nettoyer toutes les ressources une fois le TP terminé.

### Apports de Terraform par rapport à Azure CLI ou UI

Terraform présente des avantages significatifs par rapport à l'utilisation d'Azure CLI ou de l'interface utilisateur :

- Gestion comme du code : Terraform permet une gestion structurée et reproductible de l'infrastructure grâce à une approche basée sur du code, facilitant ainsi la collaboration et la gestion des versions.
- Automatisation des déploiements : Terraform permet une automatisation complète des déploiements, réduisant les erreurs humaines et assurant la cohérence des environnements.
- Planification des modifications : Terraform offre la possibilité de planifier les modifications d'infrastructure avant leur application, ce qui permet d'anticiper les impacts et de prévenir les interruptions de service.
- Gestion des variables : La gestion des variables dans Terraform simplifie la maintenance et l'évolution de l'infrastructure, permettant une configuration dynamique en fonction des environnements cibles.
