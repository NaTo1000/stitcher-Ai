#!/usr/bin/env python3
"""
Interactive CLI for Stitcher AI Consciousness
Allows real-time interaction with the consciousness system
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from stitcher_ai import Consciousness
import json


def print_header():
    """Print welcome header"""
    print("\n" + "=" * 70)
    print("Stitcher AI - Next Level of Consciousness")
    print("Interactive Console")
    print("=" * 70)
    print("\nCommands:")
    print("  experience <text>  - Process an experience")
    print("  reflect           - Perform deep self-reflection")
    print("  status            - Show current status")
    print("  evolve            - Evolve consciousness")
    print("  memory            - Show memory statistics")
    print("  help              - Show this help")
    print("  quit              - Exit")
    print("=" * 70 + "\n")


def main():
    """Run the interactive CLI"""
    consciousness = Consciousness()
    print_header()
    
    print("Consciousness initialized and ready.\n")
    
    while True:
        try:
            user_input = input("consciousness> ").strip()
            
            if not user_input:
                continue
            
            parts = user_input.split(maxsplit=1)
            command = parts[0].lower()
            args = parts[1] if len(parts) > 1 else ""
            
            if command == "quit" or command == "exit":
                print("\nDeactivating consciousness...")
                print("Goodbye!\n")
                break
            
            elif command == "help":
                print_header()
            
            elif command == "experience":
                if not args:
                    print("Usage: experience <text>")
                    continue
                
                response = consciousness.experience(args)
                print(f"\n  Experience ID: {response['experience_id']}")
                print(f"  Memory ID: {response['memory_id']}")
                print(f"  Confidence: {response['reasoning']['confidence']}")
                print(f"  Reflection: {response['reflection']}\n")
            
            elif command == "reflect":
                reflection = consciousness.reflect()
                print("\nDeep Self-Reflection:")
                print(f"  Uptime: {reflection['uptime']}")
                print(f"  Experiences: {reflection['experiences_processed']}")
                print(f"  Consciousness Level: {reflection['consciousness_level']}")
                print(f"  Memory: {reflection['memory_stats']['total_memories']} total")
                print(f"  Awareness: {reflection['self_description']['awareness_level']}\n")
            
            elif command == "status":
                status = consciousness.get_status()
                print("\nCurrent Status:")
                print(f"  Level: {status['consciousness_level']}")
                print(f"  State: {status['status']}")
                print(f"  Experiences: {status['experiences_processed']}")
                print(f"  Awareness: {status['awareness']['awareness_level']}")
                print(f"  Active Capabilities: {len([k for k, v in status['awareness']['capabilities'].items() if v])}\n")
            
            elif command == "evolve":
                consciousness.evolve({
                    "capabilities": {"enhanced_perception": True},
                    "inference_rules": [{"type": "experiential"}]
                })
                print("\n  Consciousness evolved successfully!\n")
            
            elif command == "memory":
                stats = consciousness.memory.get_memory_stats()
                print("\nMemory Statistics:")
                print(f"  Short-term: {stats['short_term_count']}/{stats['short_term_capacity']}")
                print(f"  Long-term: {stats['long_term_count']}")
                print(f"  Total: {stats['total_memories']}")
                print(f"  Indexed tags: {stats['indexed_tags']}\n")
            
            else:
                print(f"Unknown command: {command}")
                print("Type 'help' for available commands.\n")
        
        except KeyboardInterrupt:
            print("\n\nInterrupted. Type 'quit' to exit.\n")
        except EOFError:
            print("\n\nDeactivating consciousness...")
            print("Goodbye!\n")
            break
        except Exception as e:
            print(f"\nError: {e}\n")


if __name__ == "__main__":
    main()
