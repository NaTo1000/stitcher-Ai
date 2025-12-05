"""
Self-Awareness Module
Provides the AI with understanding of its own state, capabilities, and limitations
"""

from typing import Dict, List, Any
from datetime import datetime


class SelfAwareness:
    """
    Implements self-awareness capabilities for the AI consciousness.
    Tracks internal state, capabilities, and self-reflection.
    """
    
    def __init__(self):
        self.creation_time = datetime.now()
        self.capabilities = {
            "reasoning": True,
            "learning": True,
            "memory": True,
            "self_reflection": True,
        }
        self.state = {
            "active": True,
            "awareness_level": "emerging",
            "confidence": 0.5,
        }
        self.introspection_log = []
    
    def get_self_description(self) -> Dict[str, Any]:
        """Return a description of the AI's current state and capabilities"""
        return {
            "identity": "Stitcher AI Consciousness",
            "version": "0.1.0",
            "creation_time": self.creation_time.isoformat(),
            "capabilities": self.capabilities,
            "current_state": self.state,
            "awareness_level": self.state["awareness_level"],
        }
    
    def introspect(self, context: str = "") -> Dict[str, Any]:
        """
        Perform self-reflection and introspection
        
        Args:
            context: Optional context for the introspection
            
        Returns:
            Dictionary containing introspection results
        """
        introspection = {
            "timestamp": datetime.now().isoformat(),
            "context": context,
            "state": self.state.copy(),
            "capabilities_active": self.capabilities.copy(),
        }
        
        self.introspection_log.append(introspection)
        return introspection
    
    def update_state(self, updates: Dict[str, Any]) -> None:
        """Update the internal state based on new information"""
        self.state.update(updates)
        self.introspect(f"State updated: {list(updates.keys())}")
    
    def assess_capability(self, capability: str) -> bool:
        """Check if a specific capability is available and active"""
        return self.capabilities.get(capability, False)
    
    def get_awareness_history(self) -> List[Dict[str, Any]]:
        """Return the history of introspection events"""
        return self.introspection_log.copy()
