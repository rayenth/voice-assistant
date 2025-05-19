# Voice Assistant Project

## Description

Ce projet est un assistant vocal simple qui écoute votre voix, transcrit ce que vous dites grâce au modèle Whisper d'OpenAI, puis envoie le texte à un modèle LLaMA pour générer une réponse, laquelle est ensuite lue à haute voix.

Il est conçu pour les développeurs ou passionnés souhaitant expérimenter la reconnaissance vocale, la synthèse vocale et l’IA conversationnelle en Python.

---

## Fonctionnalités

- Enregistrement audio déclenché manuellement (appuyez sur Entrée pour démarrer et arrêter l'enregistrement).
- Transcription de la parole en texte avec Whisper.
- Envoi du texte transcrit à un modèle LLaMA (via API ou local) pour générer une réponse.
- Synthèse vocale de la réponse générée.
- Enregistrement des transcriptions dans un fichier texte.

---

## Technologies utilisées

- **Python 3.8+**
- [SoundDevice](https://python-sounddevice.readthedocs.io/) : pour l'enregistrement audio.
- [Whisper](https://github.com/openai/whisper) : pour la transcription vocale.
- [NumPy](https://numpy.org/) : traitement des données audio.
- [SciPy](https://scipy.org/) : gestion des fichiers audio WAV.
- [LLaMA API / Ollama](https://ollama.com/) : pour l’IA conversationnelle.
- Synthèse vocale (ex: pyttsx3, ou autre selon implémentation).

---

## Installation

1. Cloner le dépôt :

```bash
git clone https://github.com/rayenth/voice-assistant.git
cd voice-assistant
