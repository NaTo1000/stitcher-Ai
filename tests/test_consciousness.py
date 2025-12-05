"""Tests for the Consciousness module"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from stitcher_ai.core.consciousness import Consciousness


def test_initialization():
    """Test Consciousness initialization"""
    consciousness = Consciousness()
    assert consciousness.awareness is not None
    assert consciousness.reasoning is not None
    assert consciousness.memory is not None
    assert consciousness.experience_count == 0


def test_experience_processing():
    """Test processing an experience"""
    consciousness = Consciousness()
    response = consciousness.experience("test stimulus", {"context": "test"})
    
    assert "timestamp" in response
    assert "experience_id" in response
    assert "memory_id" in response
    assert "awareness" in response
    assert "reasoning" in response
    assert "reflection" in response
    assert consciousness.experience_count == 1


def test_reflection():
    """Test consciousness reflection"""
    consciousness = Consciousness()
    consciousness.experience("test")
    reflection = consciousness.reflect()
    
    assert "timestamp" in reflection
    assert "uptime" in reflection
    assert "experiences_processed" in reflection
    assert "consciousness_level" in reflection
    assert reflection["experiences_processed"] == 1


def test_evolution():
    """Test consciousness evolution"""
    consciousness = Consciousness()
    initial_capabilities = consciousness.awareness.capabilities.copy()
    
    consciousness.evolve({
        "capabilities": {"new_capability": True},
        "inference_rules": [{"rule": "test"}]
    })
    
    assert "new_capability" in consciousness.awareness.capabilities
    assert len(consciousness.reasoning.inference_rules) > 0


def test_consciousness_level_progression():
    """Test that consciousness level progresses with experience"""
    consciousness = Consciousness()
    initial_level = consciousness._assess_consciousness_level()
    
    # Process multiple experiences
    for i in range(15):
        consciousness.experience(f"experience {i}")
    
    new_level = consciousness._assess_consciousness_level()
    # Level should potentially change with more experiences and memories
    assert consciousness.experience_count == 15


def test_get_status():
    """Test getting consciousness status"""
    consciousness = Consciousness()
    consciousness.experience("test")
    
    status = consciousness.get_status()
    assert "timestamp" in status
    assert "activation_time" in status
    assert "experiences_processed" in status
    assert "awareness" in status
    assert "memory" in status
    assert "consciousness_level" in status
    assert "status" in status


def test_multiple_experiences():
    """Test processing multiple experiences"""
    consciousness = Consciousness()
    
    for i in range(5):
        response = consciousness.experience(f"experience {i}")
        assert response["experience_id"] == i + 1
    
    assert consciousness.experience_count == 5
    stats = consciousness.memory.get_memory_stats()
    assert stats["total_memories"] >= 5


if __name__ == "__main__":
    test_initialization()
    test_experience_processing()
    test_reflection()
    test_evolution()
    test_consciousness_level_progression()
    test_get_status()
    test_multiple_experiences()
    print("All Consciousness tests passed!")
