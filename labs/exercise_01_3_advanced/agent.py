"""AgentForge Exercise 01.3 — Conversational & Copilot Assistants (advanced)"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from core.agent_base import AgentBase

def main():
    agent = AgentBase(name="ex-01-3", instruction="You are a Conversational & Copilot Assistants agent.")
    print(f"Exercise 01.3 ready: {agent.name}")

if __name__ == "__main__":
    main()
