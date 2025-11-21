### Problem Statement -- the problem I'm trying to solve, and why I think it's an important or interesting problem to solve
Millions of students struggle with self-study. They often lack structured plans, personalized guidance, relevant notes, and regular evaluation. As a result, they waste time, miss important concepts, and lose confidence.
There is a need for a system that provides personalized learning support, adapts to each student’s strengths and weaknesses, and helps them progress efficiently. This is especially important in communities where access to teachers or coaching is limited.
TutorAgent aims to solve this problem by offering an AI-powered, adaptive study assistant.


### Why agents? -- Why are agents the right solution to this problem

Traditional chatbots respond passively to questions, but learning requires planning, retrieval, evaluation, and adaptation.
Agents excel at these tasks because they can:
Break problems into steps
Use tools (retrieval, memory, evaluation)
Learn from user feedback
Make decisions autonomously
TutorAgent uses ADK features such as planning, tool invocation, vector search, and evaluation loops to deliver a personalized learning experience.


### What I Created — Overall Architecture
TutorAgent is an autonomous learning assistant built using:
LLM-based planner to create personalized study plans
Vector embeddings + FAISS retriever to fetch accurate learning content
Memory system to store user progress
Evaluator tool to assess quiz answers and adapt difficulty
Interactive chat interface (notebook-based) for students to learn step-by-step


Architecture (text diagram):
User Input → Planner → Step List
             ↓
      Retriever Tool → Notes/Content
             ↓
           LLM Tutor → Explains concepts
             ↓
        Evaluator Tool → Quiz & Scoring
             ↓
            Memory → Adapt next steps

### Demo — Showing the Solution
In the Notebook demo:
1. The user enters a topic like “Photosynthesis”.
2. TutorAgent generates a 3-step personalized study plan.
3. It retrieves relevant notes using embeddings.
4. It explains concepts in simple language.
5. It then gives a short quiz.
6. Based on the answers, the agent updates difficulty and shows a revised plan.


### The Build — Tools and Technologies Used
Python (Colab/Kaggle Notebook)
ADK (Agent Development Kit)
LLM planning & decision making
Chroma / FAISS for vector retrieval
Embeddings for document search
JSON memory store for progress tracking
YouTube video for demo story
All code is documented clearly in the attached Notebook/GitHub repo.

### If I had more time, this is what I'd do
If time permitted, I would extend TutorAgent with:
Daily and weekly progress dashboards
Multilingual support
Voice-based tutoring
Parent/teacher progress reports
Deployment as a standalone web app
TutorAgent has strong potential to support millions of learners, especially in underserved communities.

