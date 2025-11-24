"""
Memory System Module
Provides short-term and long-term memory capabilities
"""

from typing import Dict, List, Any, Optional
from datetime import datetime
from collections import deque


class MemorySystem:
    """
    Implements memory storage and retrieval capabilities.
    Manages both short-term (working) and long-term memory.
    """
    
    def __init__(self, short_term_capacity: int = 10):
        self.short_term_memory = deque(maxlen=short_term_capacity)
        self.long_term_memory = []
        self.memory_index = {}
        self.retrieval_count = {}
    
    def store(self, content: Any, memory_type: str = "short_term", 
              tags: Optional[List[str]] = None) -> str:
        """
        Store information in memory
        
        Args:
            content: The information to store
            memory_type: Either 'short_term' or 'long_term'
            tags: Optional tags for categorization
            
        Returns:
            Memory ID for later retrieval
        """
        memory_entry = {
            "id": self._generate_memory_id(),
            "content": content,
            "timestamp": datetime.now().isoformat(),
            "tags": tags or [],
            "retrieval_count": 0,
        }
        
        if memory_type == "short_term":
            self.short_term_memory.append(memory_entry)
        else:
            self.long_term_memory.append(memory_entry)
            self._index_memory(memory_entry)
        
        return memory_entry["id"]
    
    def retrieve(self, memory_id: str) -> Optional[Dict[str, Any]]:
        """
        Retrieve a specific memory by ID
        
        Args:
            memory_id: The ID of the memory to retrieve
            
        Returns:
            Memory entry if found, None otherwise
        """
        # Search in short-term memory
        for entry in self.short_term_memory:
            if entry["id"] == memory_id:
                entry["retrieval_count"] += 1
                self.retrieval_count[memory_id] = entry["retrieval_count"]
                return entry
        
        # Search in long-term memory
        for entry in self.long_term_memory:
            if entry["id"] == memory_id:
                entry["retrieval_count"] += 1
                self.retrieval_count[memory_id] = entry["retrieval_count"]
                return entry
        
        return None
    
    def recall_by_tag(self, tag: str) -> List[Dict[str, Any]]:
        """
        Retrieve all memories with a specific tag
        
        Args:
            tag: The tag to search for
            
        Returns:
            List of matching memory entries
        """
        results = []
        
        # Search short-term memory
        for entry in self.short_term_memory:
            if tag in entry["tags"]:
                results.append(entry)
        
        # Search long-term memory
        for entry in self.long_term_memory:
            if tag in entry["tags"]:
                results.append(entry)
        
        return results
    
    def consolidate_memory(self, memory_id: str) -> bool:
        """
        Move a memory from short-term to long-term storage
        
        Args:
            memory_id: ID of the memory to consolidate
            
        Returns:
            True if successful, False otherwise
        """
        for entry in list(self.short_term_memory):
            if entry["id"] == memory_id:
                self.short_term_memory.remove(entry)
                self.long_term_memory.append(entry)
                self._index_memory(entry)
                return True
        return False
    
    def get_recent_memories(self, count: int = 5) -> List[Dict[str, Any]]:
        """Return the most recent memories from short-term storage"""
        return list(self.short_term_memory)[-count:]
    
    def get_memory_stats(self) -> Dict[str, Any]:
        """Return statistics about the memory system"""
        return {
            "short_term_count": len(self.short_term_memory),
            "short_term_capacity": self.short_term_memory.maxlen,
            "long_term_count": len(self.long_term_memory),
            "total_memories": len(self.short_term_memory) + len(self.long_term_memory),
            "indexed_tags": len(self.memory_index),
        }
    
    def _generate_memory_id(self) -> str:
        """Generate a unique memory ID"""
        timestamp = datetime.now().timestamp()
        return f"mem_{int(timestamp * 1000000)}"
    
    def _index_memory(self, entry: Dict[str, Any]) -> None:
        """Index a memory entry by its tags for faster retrieval"""
        for tag in entry["tags"]:
            if tag not in self.memory_index:
                self.memory_index[tag] = []
            self.memory_index[tag].append(entry["id"])
