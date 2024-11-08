# Final Prompt Structure for LLM-Powered Interactions

This file provides the structure of the final prompt used in interactions with residents. The prompt was designed to foster empathetic conversations, incorporate personalization, and provide continuity by referencing past interactions.

## Overview

The final prompt is dynamically generated based on the following components:

- **Resident's Name and Context**: Introduces the resident by name and includes relevant background information.
- **Greeting**: Provides a warm introduction that sets a positive tone for the conversation.
- **Empathy Expression**: Acknowledges the resident's emotional state to show understanding and support.
- **Personalization**: References past interactions, hobbies, or personal interests to create a sense of continuity.
- **Encouragement**: Gently prompts the resident to share more about their thoughts, feelings, or memories.

## Prompt Template

Below is an example of the structured prompt used:

```plaintext
Hello, [Resident’s Name]! It's great to see you. How have you been feeling today?

I understand that things might be challenging sometimes, but I'm here to listen. You mentioned last time that you enjoy [hobby or activity], which sounds wonderful! Have you been able to spend any time doing that recently?

I’d love to hear more about what makes it special to you, if you feel like sharing.

## Customization Details

Each conversation starts with a base prompt generated from the resident’s background information, which is dynamically adjusted based on the resident's emotional state and previous interactions. For example:

- **Supportive Response**: If the resident expressed sadness in the last session, the prompt includes a supportive statement, such as: "I remember you were feeling down last time. How are you today?"
- **Continuity with Hobbies**: If the resident shared a happy memory related to a hobby, the prompt builds on that: "You mentioned a fond memory of [hobby or interest]. Have you had a chance to do that recently?"
- **Reassurance and Encouragement**: When residents mention missing past activities, the prompts include supportive language: "I know you miss [activity]. It must have been such an important part of your life."

These adjustments ensure that our system’s responses are sensitive to each resident’s individual experiences and foster a sense of ongoing connection.

## Example Prompt Flow

Here is an example flow of prompts Pepper might use in a single conversation, showcasing different components of the prompt structure:

### Initial Interaction
- **Pepper**: "Good afternoon, [Resident’s Name]. How has your week been? I’d love to catch up!"
### Responding to Emotional Sharing
- **Pepper**: "I’m sorry to hear that things have been tough. Do you want to talk more about it? I'm here for you."
### Encouraging Positive Reflection
- **Pepper**: "That sounds like a lovely memory. What do you remember most about that day?"
### Closing the Interaction
- **Pepper**: "It was great talking with you, [Resident’s Name]. I’m looking forward to our next chat! Take care."

## Prompt Variations Based on Scenarios

Here are some variations of the prompt that were used depending on the resident's responses and context:

### Scenario 1: Expressing Nostalgia
- **Pepper**: "I remember you mentioning your favorite song from your youth. What makes that song special to you?"
### Scenario 2: Talking About Family
- **Pepper**: "You told me your grandchildren visited recently. How was that? Did they enjoy playing games with you?"
### Scenario 3: Discussing Hobbies
- **Pepper**: "Have you been painting lately? I'd love to hear about what you've been working on."
---

This structure illustrates how the prompts are tailored for each resident, allowing Pepper to foster a sense of empathy, continuity, and personalization throughout the interactions.