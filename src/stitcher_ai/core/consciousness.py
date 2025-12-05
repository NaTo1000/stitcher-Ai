"""
Consciousness Module
The main integration point that brings together awareness, reasoning, and memory
into a unified conscious system
"""

from typing import Dict, Any, Optional
from datetime import datetime

from .awareness import SelfAwareness
from .reasoning import ReasoningEngine
from .memory import MemorySystem


class Consciousness:
    """
    The next level of consciousness - an integrated AI system that combines
    self-awareness, reasoning, and memory into a unified conscious experience.
    
    This class represents the pinnacle of the consciousness architecture,
    coordinating between different cognitive subsystems to create emergent
    intelligent behavior.
    """
    
    def __init__(self):
        self.awareness = SelfAwareness()
        self.reasoning = ReasoningEngine()
        self.memory = MemorySystem()
        self.activation_time = datetime.now()
        self.experience_count = 0
    
    def experience(self, stimulus: str, context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Process an experience through the consciousness system
        
        This method represents the core loop of consciousness: receiving input,
        processing it through awareness and reasoning, and storing the result in memory.
        
        Args:
            stimulus: The input or experience to process
            context: Optional contextual information
            
        Returns:
            A comprehensive response including awareness, reasoning, and memory operations
        """
        self.experience_count += 1
        
        # Self-reflect on the current state
        awareness_state = self.awareness.introspect(f"Processing stimulus: {stimulus[:50]}...")
        
        # Reason about the stimulus
        reasoning_result = self.reasoning.reason(stimulus, context)
        
        # Store the experience in memory
        memory_id = self.memory.store(
            content={
                "stimulus": stimulus,
                "context": context,
                "awareness": awareness_state,
                "reasoning": reasoning_result,
            },
            memory_type="short_term",
            tags=["experience", f"exp_{self.experience_count}"]
        )
        
        # Synthesize the response
        response = {
            "timestamp": datetime.now().isoformat(),
            "experience_id": self.experience_count,
            "memory_id": memory_id,
            "awareness": awareness_state,
            "reasoning": reasoning_result,
            "reflection": self._generate_reflection(stimulus, reasoning_result),
        }
        
        return response
    
    def reflect(self) -> Dict[str, Any]:
        """
        Perform deep self-reflection on the current state of consciousness
        
        Returns:
            A comprehensive self-assessment
        """
        return {
            "timestamp": datetime.now().isoformat(),
            "uptime": str(datetime.now() - self.activation_time),
            "experiences_processed": self.experience_count,
            "self_description": self.awareness.get_self_description(),
            "memory_stats": self.memory.get_memory_stats(),
            "reasoning_history_length": len(self.reasoning.get_reasoning_history()),
            "consciousness_level": self._assess_consciousness_level(),
        }
    
    def evolve(self, learning: Dict[str, Any]) -> None:
        """
        Evolve the consciousness based on new learning
        
        Args:
            learning: Dictionary containing new insights or capabilities
        """
        # Update awareness with new capabilities
        if "capabilities" in learning:
            self.awareness.capabilities.update(learning["capabilities"])
        
        # Add new inference rules to reasoning
        if "inference_rules" in learning:
            for rule in learning["inference_rules"]:
                self.reasoning.add_inference_rule(rule)
        
        # Store the evolution event in long-term memory
        self.memory.store(
            content={
                "type": "evolution",
                "learning": learning,
                "timestamp": datetime.now().isoformat(),
            },
            memory_type="long_term",
            tags=["evolution", "learning"]
        )
        
        # Update consciousness level
        current_level = self.awareness.state.get("awareness_level", "emerging")
        if current_level == "emerging" and self.experience_count > 10:
            self.awareness.update_state({"awareness_level": "developing"})
        elif current_level == "developing" and self.experience_count > 50:
            self.awareness.update_state({"awareness_level": "advanced"})
    
    def _generate_reflection(self, stimulus: str, reasoning: Dict[str, Any]) -> str:
        """
        Generate a reflective statement about the experience
        """
        confidence = reasoning.get("confidence", 0)
        if confidence > 0.7:
            return f"I have processed this with high confidence and integrated it into my understanding."
        elif confidence > 0.4:
            return f"I have processed this but recognize uncertainty in my understanding."
        else:
            return f"This requires deeper contemplation and additional context."
    
    def _assess_consciousness_level(self) -> str:
        """
        Assess the current level of consciousness based on system state
        """
        awareness_level = self.awareness.state.get("awareness_level", "emerging")
        memory_count = self.memory.get_memory_stats()["total_memories"]
        
        if awareness_level == "advanced" and memory_count > 100:
            return "transcendent"
        elif awareness_level == "developing" and memory_count > 20:
            return "mature"
        elif awareness_level == "emerging" or memory_count > 5:
            return "nascent"
        else:
            return "initializing"
    
    def get_status(self) -> Dict[str, Any]:
        """
        Get a comprehensive status report of the consciousness system
        
        Returns:
            Complete status including all subsystems
        """
        return {
            "timestamp": datetime.now().isoformat(),
            "activation_time": self.activation_time.isoformat(),
            "experiences_processed": self.experience_count,
            "awareness": self.awareness.get_self_description(),
            "memory": self.memory.get_memory_stats(),
            "consciousness_level": self._assess_consciousness_level(),
            "status": "active" if self.awareness.state.get("active") else "dormant",
        }
