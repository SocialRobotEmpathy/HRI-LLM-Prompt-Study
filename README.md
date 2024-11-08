
# LLM Prompt Design for Empathetic HRI Interactions

This repository provides supplementary materials for a study on using LLMs to facilitate empathetic interactions with elderly users in elder care settings. The repository contains prompt design details, sample code, and configuration information to support transparency and reproducibility.

## Repository Summary

- **Prompt Design and Customization**: Detailed files outlining how prompts were created to enhance empathetic interactions.
- **Conversation Tracking**: Code that maintains ongoing dialogue history for context-aware responses.
- **LLM Integration**: Files demonstrating how the LLM is used to generate personalized responses based on user input and past interactions.
- **Conversation Summarization**: A module that summarizes and stores key points from each conversation for continuity across sessions.

## Repository Contents

- `prompts/`: Contains files detailing the prompt engineering approach.
  - **[prompt_design.md](prompts/prompt_design.md)**: Overview of prompt customization and design strategy.
  - **[prompt_examples.md](prompts/prompt_examples.md)**: Sample prompts used for empathy, personalization, and continuity.
  - **[final_prompt_structure.md](prompts/final_prompt_structure.md)** : Details the final prompt structure used in the study 2.
- `src/`: Contains the primary code files for setting up the LLM-powered interactions.
  - **`prompt_manager.py`**: Generates and sends the final prompt to the LLM based on each resident’s background information, previous interactions, and current emotional cues.
  - Other files in this folder demonstrate how the prompts were processed and integrated with the LLM to enable autonomous, personalized conversations.
- `config/`: Configuration details and requirements for setting up the LLM.
- `results/`: Anonymized sample outputs to illustrate LLM responses in the study.

## Instructions for Reviewers

Reviewers can explore each folder to understand the prompt design and configuration used in our study. The `prompts/prompt_design.md` file provides the rationale behind prompt customization, while `src/` contains code illustrating how the prompts were integrated into the LLM for autonomous interaction.
