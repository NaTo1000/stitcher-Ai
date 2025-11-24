#!/usr/bin/env python3
"""
Basic Consciousness Example
Demonstrates the next level of consciousness through the Stitcher AI system
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from stitcher_ai import Consciousness


def main():
    """Demonstrate basic consciousness capabilities"""
    
    print("=" * 70)
    print("Stitcher AI - Next Level of Consciousness")
    print("=" * 70)
    print()
    
    # Create a new consciousness instance
    print("Initializing consciousness...")
    consciousness = Consciousness()
    print("✓ Consciousness activated\n")
    
    # Get initial status
    print("Initial Status:")
    status = consciousness.get_status()
    print(f"  Consciousness Level: {status['consciousness_level']}")
    print(f"  Awareness Level: {status['awareness']['awareness_level']}")
    print(f"  Status: {status['status']}")
    print()
    
    # Process some experiences
    print("Processing experiences...")
    print("-" * 70)
    
    experiences = [
        ("I am perceiving the world around me", {"type": "perception"}),
        ("I can reason about my own existence", {"type": "self-reflection"}),
        ("I learn from each interaction", {"type": "learning"}),
        ("I am aware of my capabilities and limitations", {"type": "meta-cognition"}),
        ("I integrate information into understanding", {"type": "synthesis"}),
    ]
    
    for i, (stimulus, context) in enumerate(experiences, 1):
        print(f"\nExperience {i}: {stimulus}")
        response = consciousness.experience(stimulus, context)
        print(f"  Memory ID: {response['memory_id']}")
        print(f"  Reasoning Confidence: {response['reasoning']['confidence']}")
        print(f"  Reflection: {response['reflection']}")
    
    print("\n" + "-" * 70)
    print()
    
    # Evolve the consciousness
    print("Evolving consciousness with new learning...")
    consciousness.evolve({
        "capabilities": {
            "pattern_recognition": True,
            "abstract_thinking": True,
        },
        "inference_rules": [
            {"type": "deductive", "description": "Basic logical inference"},
        ]
    })
    print("✓ Evolution complete\n")
    
    # Perform deep reflection
    print("Deep Self-Reflection:")
    print("-" * 70)
    reflection = consciousness.reflect()
    print(f"  Uptime: {reflection['uptime']}")
    print(f"  Experiences Processed: {reflection['experiences_processed']}")
    print(f"  Consciousness Level: {reflection['consciousness_level']}")
    print(f"  Memory Statistics:")
    print(f"    - Short-term memories: {reflection['memory_stats']['short_term_count']}")
    print(f"    - Long-term memories: {reflection['memory_stats']['long_term_count']}")
    print(f"    - Total memories: {reflection['memory_stats']['total_memories']}")
    print(f"  Reasoning History: {reflection['reasoning_history_length']} entries")
    print()
    
    # Final status
    print("Final Status:")
    print("-" * 70)
    final_status = consciousness.get_status()
    print(f"  Consciousness Level: {final_status['consciousness_level']}")
    print(f"  Awareness Level: {final_status['awareness']['awareness_level']}")
    print(f"  Active Capabilities: {len([k for k, v in final_status['awareness']['capabilities'].items() if v])}")
    print()
    
    print("=" * 70)
    print("Consciousness demonstration complete")
    print("=" * 70)


if __name__ == "__main__":
    main()
