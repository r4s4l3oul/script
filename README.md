# Scripts

Ce dépôt regroupe différents scripts Python développés dans le cadre de mon apprentissage en cybersécurité.

L'objectif est de concevoir des outils simples permettant d'automatiser certaines tâches, de mettre en pratique des concepts de sécurité informatique et d'implémenter différents algorithmes étudiés au cours de ma formation.

---

## Objectifs

- Développer des outils utiles en cybersécurité.
- Approfondir ma maîtrise de Python.
- Implémenter des algorithmes cryptographiques.
- Automatiser des tâches courantes.
- Documenter mes travaux de manière claire et progressive.

---

# Structure du dépôt

```text
scripts/
│
├── automation/
│   ├── ...
│
├── cryptographie/
│   ├── cesar/
│   ├── vigenere/
│   ├── xor/
│   ├── affine/
│   ├── rsa/
│   └── aes/
│
├── forensic/
│
├── reseau/
│
├── web/
│
├── utilitaires/
│
└── README.md
```

---

# Contenu

## Cryptographie

Implémentation de différents algorithmes de chiffrement et de déchiffrement.

Exemples :

- Chiffrement de César
- Chiffrement de Vigenère
- Chiffrement XOR
- Chiffrement affine
- RSA
- AES

Les scripts ont pour objectif de comprendre le fonctionnement des algorithmes avant d'utiliser des bibliothèques spécialisées.

---

## Automatisation

Scripts permettant d'automatiser différentes tâches.

Exemples :

- organisation de fichiers ;
- analyse de journaux (logs) ;
- renommage automatique ;
- traitement de données.

---

## Réseau

Outils liés aux réseaux.

Exemples :

- scanner de ports ;
- client/serveur TCP ;
- utilitaires réseau ;
- scripts utilisant les sockets Python.

---

## Web

Scripts destinés à la sécurité des applications web.

Exemples :

- manipulation de JWT ;
- calcul de hash ;
- encodage / décodage ;
- outils HTTP.

---

## Forensic

Scripts d'analyse de fichiers.

Exemples :

- extraction de métadonnées ;
- identification de signatures de fichiers ;
- calcul d'empreintes (hash).

---

## Utilitaires

Divers scripts pouvant être réutilisés dans d'autres projets.

---

# Technologies

- Python 3
- Bibliothèque standard Python
- argparse
- hashlib
- socket
- pathlib
- requests
- cryptography (lorsque nécessaire)

---

# Philosophie du projet

L'objectif de ce dépôt est avant tout pédagogique.

Chaque script est développé afin de comprendre le fonctionnement interne des techniques utilisées plutôt que de simplement employer des outils existants.

Les implémentations privilégient la simplicité, la lisibilité et la compréhension des concepts.

---
