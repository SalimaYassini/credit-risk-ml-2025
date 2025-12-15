import streamlit as st
st.set_page_config(page_title="Aide & Explications – Salima Yassini 2025", layout="wide")
st.image("https://via.placeholder.com/1200x300/000000/FFFFFF?text=Credit+Risk+Scoring+France+2025+-+Salima+Yassini", use_container_width=True)
st.title("Comment fonctionne le scoring crédit IA + expertise terrain de France")
st.markdown("#### Par Salima Yassini – 15 ans d’expérience – DSO 90 → 25 jours – +3,9 M€ de cash récupéré")
st.success("Cet outil ne remplace pas le Credit Manager… **il le rend 10 fois plus rapide et 100 fois plus crédible en comité crédit.**")

# ===================================================================
# 1. LE VRAI RISQUE VS LE RISQUE BRUT
# ===================================================================
st.markdown("### 1. Il existe deux risques (et un seul compte vraiment)")
col1, col2 = st.columns(2)
with col1:
    st.error("**Risque brut IA**")
    st.write("""
    - Calculé uniquement sur les chiffres bruts
    - Très bon (AUC 0.9412)
    - Mais parfois trop sévère : il ne connaît pas vos litiges, vos clients stratégiques, vos délais contractuels
    """)
with col2:
    st.success("**Risque réel ajusté Salima Yassini** ← celui-là qu’il faut regarder")
    st.write("""
    - Le même modèle IA
    - + mes 15 ans d’expérience intégrés
    - Fonds propres négatifs, trésorerie négative, autonomie < 20 % → **ALERTE ROUGE immédiate**
    - Litige bloquant ou client stratégique → le score peut tomber à 3-5 %
    """)

# ===================================================================
# 2. LES 10 PARAMÈTRES CLÉS À SAISIR
# ===================================================================
st.markdown("### 2. Les 10 paramètres clés à saisir (même un novice y arrive en 1 minute)")
st.info("""
1. Chiffre d’affaires HT 2024 (global du client – pour le scoring IA)
2. Résultat net 2024
3. Total bilan
4. Fonds propres
5. Trésorerie nette
6. Emprunts & dettes financières
7. Délai accordé + retard moyen → DSO réel
8. Score externe (Ellisphere/Altares/Coface, Infolégale...)
9. Région & Secteur
10. CA TTC annuel réalisé N-1 ou prévisionnel N avec ce client (€) – **clé pour la limite de crédit proposée**
""")

# ===================================================================
# 3. LES ALERTES
# ===================================================================
st.markdown("### 3. Les alertes automatiques")
st.error("""
**ALERTE ROUGE IMMÉDIATE dès que :**
- Fonds propres négatifs
- Trésorerie négative
- Autonomie financière < 20 %
- DSO > 110 jours
→ Même si vous cochez « client stratégique », l’outil reste sévère (car en réalité, ces entreprises finissent souvent mal)
""")

# ===================================================================
# 4. COMMENT ÇA MARCHE EN 30 SECONDES
# ===================================================================
st.markdown("### 4. Comment l’utiliser (même si vous n’êtes pas Credit Manager)")
st.info("""
1. Remplissez les 10 paramètres clés
2. Cochez la réalité terrain en 10 secondes :
   - Litige bloquant ? → cochez
   - Client stratégique ? → cochez
3. Cliquez sur **« PRÉDIRE LE RISQUE »**
→ Vous avez immédiatement :
   - Le risque brut IA
   - Le **vrai risque ajusté par Salima Yassini**
   - La **limite de crédit proposée** (en gros vert ou rouge selon la situation)
   - Les actions à faire (blocage livraison, injonction, etc.)
   - Historique complet + export Excel en 1 clic
""")

# ===================================================================
# 5. POUR QUI CET OUTIL EST FAIT
# ===================================================================
st.markdown("### 5. Cet outil est fait pour vous si vous êtes…")
st.markdown("""
- **Credit Manager** → gagnez 3 h par jour sur vos analyses
""")
st.markdown("""
- **DAF / Dirigeant → comprenez enfin pourquoi un client à 90 jours n’est pas forcément mort**
Un client à 90 jours de retard = alerte rouge chez 99 % des dirigeants.
Mais en réalité (15 ans d’expérience terrain) :
70 % des retards > 90 jours sont **administratifs** (litige facture, avoir en attente, bon de réception non signé…)
Le client est souvent **stratégique** (gros CA, historique, relation DG)
Il finit **quasiment toujours** par payer (souvent à 120-150 jours, mais il paye)
Mon IA intègre ça :
Un client à 115 jours + litige en cours + client stratégique → **risque réel = 4-8 %** (pas 75 % comme les scores externes)
Vous voyez enfin **pourquoi le Credit Manager dit « on le garde »** en comité crédit
Et vous gardez **2 à 5 M€ de CA supplémentaire par an** sans prendre de risque réel
**C’est exactement pour ça que cet outil existe.**
""")
st.markdown("""
- **Commercial** → justifiez enfin à votre boss pourquoi vous gardez ce gros client qui paye lentement
- **Assureur-crédit** → comparez votre score avec le mien (vous allez être surpris)
""")

# ===================================================================
# 6. HISTORIQUE & EXPORT EXCEL
# ===================================================================
st.markdown("### 6. Historique par client & Export Excel magique")
st.success("""
Toutes vos simulations sont sauvegardées automatiquement avec :
- Nom client + SIREN
- Risque brut + risque ajusté
- Niveau de risque
- Vos commentaires terrain
Un clic → fichier Excel prêt à coller en comité crédit ou chez votre assureur-crédit
""")

# ===================================================================
# 7. LA LIMITE DE CRÉDIT PROPOSÉE (nouvelle fonctionnalité 2025)
# ===================================================================
st.markdown("### 7. La limite de crédit proposée – calcul automatique et intelligent")
st.success("L’outil calcule désormais une **limite de crédit cible** basée sur votre exposition réelle au client, affichée en gros pour un impact immédiat en comité crédit.")
st.markdown("""
**Formule de base** (standard crédit management) :
**Limite brute = (CA TTC annuel réalisé N-1 ou prévisionnel N avec ce client × Délai accordé sur facture en jours) / 365**

Cette base représente le plafond théorique si le client paie exactement au délai accordé.

**Ajustements terrain réalistes** (basés sur 15 ans d’expérience) :
- **Nombre de relances** : -8 % par relance après la première (signe de problème cash).
- **Type de client** : multiplicateur selon le risque historique :
  - Grand Compte : × 1.35 (+35 %) – volume important, paiement fiable.
  - ETI : × 1.20 (+20 %) – bon équilibre.
  - Administration publique : × 1.40 (+40 %) – paiement lent mais sûr à 100 %.
  - PME : × 1.0 (neutre) – référence standard.
  - International : × 0.90 (-10 %) – risque devise/juridiction.
  - Startup : × 0.70 (-30 %) – haut risque défaut.
- **Litige en cours** : -30 % (blocage paiement = risque immédiat).
- **Client stratégique** : +20 % (on accepte plus de risque pour garder un gros CA).

**En cas de situation critique** (fonds propres négatifs, autonomie < 20 %, trésorerie négative, DSO > 110 jours) :
**Limite proposée forcée à 0 €** (affichée en rouge) + message clair + actions prioritaires (garanties, paiement comptant, blocage).

**Risque net exposé** (affiché en info) :
Limite proposée – Montant couvert par garantie/assurance (en €).
Vous voyez immédiatement combien vous reste exposé après couverture.

**Encours actuel** : utilisé pour détecter les dépassements et alerter (mais ne réduit pas la limite brute – la limite est le plafond cible).

**Exemple** : CA TTC avec client = 2 400 000 €, Délai = 45 jours, Garantie = 100 000 €, Relances = 0, Type = PME, Pas de litige/stratégique, Encours = 50 000 €
→ Limite brute ≈ 295 890 € → Limite proposée ≈ 295 890 € → Risque net exposé ≈ 195 890 € après garantie.

Cette limite est **prudente, réaliste et prête à coller en comité crédit**.
""")

# ===================================================================
# 8. FOOTER
# ===================================================================
st.markdown("---")
st.markdown("""
**Outil créé en décembre 2025 par Salima Yassini**
**Contact :** safia142001@yahoo.fr • 07 78 24 78 49
**LinkedIn :** [Salima Yassini](https://www.linkedin.com/in/salima-yassini-1565b8398/)
""")
