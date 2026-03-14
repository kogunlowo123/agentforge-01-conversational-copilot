"""AgentForge Exercise 01.1 — Conversational & Copilot Assistants (beginner)"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from core.agent_base import AgentBase

def main():
    agent = AgentBase(name="ex-01-1", instruction="You are a Conversational & Copilot Assistants agent.")
    print(f"Exercise 01.1 ready: {agent.name}")

if __name__ == "__main__":
    main()
