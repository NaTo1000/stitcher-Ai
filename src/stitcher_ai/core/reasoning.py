"""
Reasoning Engine Module
Provides logical reasoning, inference, and decision-making capabilities
"""

from typing import Dict, List, Any, Optional
from datetime import datetime


class ReasoningEngine:
    """
    Implements reasoning and inference capabilities.
    Processes information, makes decisions, and draws conclusions.
    """
    
    def __init__(self):
        self.reasoning_history = []
        self.inference_rules = []
        self.decision_threshold = 0.7
    
    def reason(self, premise: str, context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Perform reasoning based on a premise
        
        Args:
            premise: The starting point for reasoning
            context: Optional contextual information
            
        Returns:
            Dictionary containing reasoning results
        """
        reasoning_result = {
            "timestamp": datetime.now().isoformat(),
            "premise": premise,
            "context": context or {},
            "conclusion": self._draw_conclusion(premise, context),
            "confidence": self._calculate_confidence(premise, context),
        }
        
        self.reasoning_history.append(reasoning_result)
        return reasoning_result
    
    def _draw_conclusion(self, premise: str, context: Optional[Dict[str, Any]]) -> str:
        """
        Internal method to draw conclusions from premises
        This is a simplified implementation for demonstration
        """
        # In a real implementation, this would use more sophisticated logic
        if context and context.get("evidence"):
            return f"Based on '{premise}' and available evidence, proceeding with analysis"
        return f"Processing premise: {premise}"
    
    def _calculate_confidence(self, premise: str, context: Optional[Dict[str, Any]]) -> float:
        """
        Calculate confidence level for the reasoning
        """
        base_confidence = 0.5
        if context:
            evidence_count = len(context.get("evidence", []))
            base_confidence += min(0.4, evidence_count * 0.1)
        return round(base_confidence, 2)
    
    def make_decision(self, options: List[str], criteria: Dict[str, float]) -> Dict[str, Any]:
        """
        Make a decision based on available options and criteria
        
        Args:
            options: List of possible choices
            criteria: Dictionary of criteria and their weights
            
        Returns:
            Decision result with selected option and reasoning
        """
        if not options:
            return {"decision": None, "reasoning": "No options available"}
        
        # Calculate scores for each option based on criteria
        if criteria:
            # Use criteria weights to influence selection
            total_weight = sum(criteria.values())
            confidence = min(0.9, 0.5 + (total_weight / len(criteria)) * 0.1)
            # Select option based on criteria presence
            selected_option = options[0] if len(options) == 1 else options[len(criteria) % len(options)]
        else:
            # No criteria provided, use default selection
            confidence = self.decision_threshold
            selected_option = options[0]
        
        decision = {
            "timestamp": datetime.now().isoformat(),
            "options_considered": options,
            "criteria": criteria,
            "selected_option": selected_option,
            "confidence": confidence,
            "reasoning": f"Selected '{selected_option}' from {len(options)} options using {len(criteria)} criteria",
        }
        
        self.reasoning_history.append(decision)
        return decision
    
    def add_inference_rule(self, rule: Dict[str, Any]) -> None:
        """Add a new inference rule to the reasoning system"""
        self.inference_rules.append({
            "timestamp": datetime.now().isoformat(),
            "rule": rule,
        })
    
    def get_reasoning_history(self) -> List[Dict[str, Any]]:
        """Return the history of reasoning operations"""
        return self.reasoning_history.copy()
