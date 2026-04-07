# Schafkopf AI Coach

A local AI-powered coach for the Bavarian card game Schafkopf. It analyzes game states, computes valid moves, and recommends the best play using a local LLM.

## Architecture

The app uses a LangGraph agent workflow:

```
rules → strategy → END
```

- **Rules Agent** — computes valid moves from the current game state
- **Strategy Agent** — asks a local LLM for the best move with an explanation

## Tech Stack

- Python 3.14
- LangGraph (agent orchestration)
- Ollama with Gemma 4 (local LLM)

## Setup

```bash
# Clone and install
git clone https://github.com/lesmuc/schafkopf-ai-coach.git
cd schafkopf-ai-coach
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Start Ollama with Gemma 4
ollama serve
ollama pull gemma4

# Run
python -m app.main
```

## Example Output

```
Bester Zug: HZ
Begründung: Der Vorzug des Mitspielens gilt immer, wenn möglich...
```

## Tests

```bash
pytest
```
