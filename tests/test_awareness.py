"""Tests for the SelfAwareness module"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from stitcher_ai.core.awareness import SelfAwareness


def test_initialization():
    """Test that SelfAwareness initializes correctly"""
    awareness = SelfAwareness()
    assert awareness.creation_time is not None
    assert awareness.capabilities["reasoning"] is True
    assert awareness.state["active"] is True
    assert awareness.state["awareness_level"] == "emerging"


def test_get_self_description():
    """Test self-description generation"""
    awareness = SelfAwareness()
    description = awareness.get_self_description()
    assert "identity" in description
    assert "capabilities" in description
    assert "current_state" in description
    assert description["awareness_level"] == "emerging"


def test_introspection():
    """Test introspection capability"""
    awareness = SelfAwareness()
    result = awareness.introspect("test context")
    assert "timestamp" in result
    assert "context" in result
    assert result["context"] == "test context"
    assert "state" in result
    assert len(awareness.introspection_log) == 1


def test_state_update():
    """Test state updating"""
    awareness = SelfAwareness()
    initial_log_length = len(awareness.introspection_log)
    awareness.update_state({"awareness_level": "advanced"})
    assert awareness.state["awareness_level"] == "advanced"
    assert len(awareness.introspection_log) > initial_log_length


def test_assess_capability():
    """Test capability assessment"""
    awareness = SelfAwareness()
    assert awareness.assess_capability("reasoning") is True
    assert awareness.assess_capability("nonexistent") is False


def test_awareness_history():
    """Test introspection history"""
    awareness = SelfAwareness()
    awareness.introspect("first")
    awareness.introspect("second")
    history = awareness.get_awareness_history()
    assert len(history) == 2
    assert history[0]["context"] == "first"
    assert history[1]["context"] == "second"


if __name__ == "__main__":
    test_initialization()
    test_get_self_description()
    test_introspection()
    test_state_update()
    test_assess_capability()
    test_awareness_history()
    print("All SelfAwareness tests passed!")
