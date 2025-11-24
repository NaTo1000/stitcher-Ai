"""Tests for the MemorySystem module"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from stitcher_ai.core.memory import MemorySystem


def test_initialization():
    """Test MemorySystem initialization"""
    memory = MemorySystem(short_term_capacity=5)
    assert len(memory.short_term_memory) == 0
    assert len(memory.long_term_memory) == 0


def test_short_term_storage():
    """Test storing in short-term memory"""
    memory = MemorySystem()
    memory_id = memory.store("test content", memory_type="short_term", tags=["test"])
    assert memory_id.startswith("mem_")
    assert len(memory.short_term_memory) == 1


def test_long_term_storage():
    """Test storing in long-term memory"""
    memory = MemorySystem()
    memory_id = memory.store("test content", memory_type="long_term", tags=["test"])
    assert memory_id.startswith("mem_")
    assert len(memory.long_term_memory) == 1


def test_retrieval():
    """Test memory retrieval"""
    memory = MemorySystem()
    memory_id = memory.store("test content", memory_type="short_term")
    retrieved = memory.retrieve(memory_id)
    assert retrieved is not None
    assert retrieved["content"] == "test content"
    assert retrieved["retrieval_count"] == 1


def test_recall_by_tag():
    """Test recalling memories by tag"""
    memory = MemorySystem()
    memory.store("content1", memory_type="short_term", tags=["tag1", "tag2"])
    memory.store("content2", memory_type="short_term", tags=["tag1"])
    memory.store("content3", memory_type="long_term", tags=["tag2"])
    
    tag1_results = memory.recall_by_tag("tag1")
    tag2_results = memory.recall_by_tag("tag2")
    
    assert len(tag1_results) == 2
    assert len(tag2_results) == 2


def test_consolidation():
    """Test memory consolidation from short to long term"""
    memory = MemorySystem()
    memory_id = memory.store("test content", memory_type="short_term")
    
    initial_short = len(memory.short_term_memory)
    initial_long = len(memory.long_term_memory)
    
    success = memory.consolidate_memory(memory_id)
    
    assert success is True
    assert len(memory.short_term_memory) == initial_short - 1
    assert len(memory.long_term_memory) == initial_long + 1


def test_recent_memories():
    """Test getting recent memories"""
    memory = MemorySystem()
    for i in range(5):
        memory.store(f"content{i}", memory_type="short_term")
    
    recent = memory.get_recent_memories(count=3)
    assert len(recent) == 3


def test_memory_stats():
    """Test memory statistics"""
    memory = MemorySystem(short_term_capacity=10)
    memory.store("short", memory_type="short_term", tags=["tag1"])
    memory.store("long", memory_type="long_term", tags=["tag2"])
    
    stats = memory.get_memory_stats()
    assert stats["short_term_count"] == 1
    assert stats["long_term_count"] == 1
    assert stats["total_memories"] == 2
    assert stats["short_term_capacity"] == 10


if __name__ == "__main__":
    test_initialization()
    test_short_term_storage()
    test_long_term_storage()
    test_retrieval()
    test_recall_by_tag()
    test_consolidation()
    test_recent_memories()
    test_memory_stats()
    print("All MemorySystem tests passed!")
