"""
Base Task class for AI Content Studio

This module provides the foundation for all specialized tasks in the content studio.
It includes common functionality like task execution, validation, and result handling.
"""

import logging
from typing import Dict, Any, Optional, List
from crewai import Task
from app.agents.base_agent import BaseAgent


class BaseTask:
    """Base class for all content creation tasks"""
    
    def __init__(self, name: str, description: str, agent: BaseAgent, expected_output: str = ""):
        """
        Initialize base task
        
        Args:
            name: Task name
            description: Task description
            agent: Agent to execute the task
            expected_output: Expected output format
        """
        self.name = name
        self.description = description
        self.agent = agent
        self.expected_output = expected_output
        self.logger = logging.getLogger(f"task.{name.lower().replace(' ', '_')}")
        
        # Create CrewAI task
        self.task = Task(
            description=description,
            agent=agent.agent,
            expected_output=expected_output
        )
    
    def execute(self, context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Execute the task
        
        Args:
            context: Additional context for task execution
            
        Returns:
            Dict containing task execution results
        """
        try:
            self.logger.info(f"Executing task: {self.name}")
            
            # Prepare task input
            task_input = self.description
            if context:
                task_input += f"\n\nContext: {context}"
            
            # Execute task using CrewAI
            result = self.task.execute()
            
            self.logger.info(f"Task completed successfully")
            return self._process_result(result)
            
        except Exception as e:
            self.logger.error(f"Error executing task: {str(e)}")
            raise
    
    def _process_result(self, result: str) -> Dict[str, Any]:
        """
        Process task result
        
        Args:
            result: Raw task result
            
        Returns:
            Dict containing processed result
        """
        return {
            "task_name": self.name,
            "result": result,
            "status": "completed",
            "agent_used": self.agent.name
        }
    
    def validate_input(self, input_data: Any) -> bool:
        """
        Validate input data for the task
        
        Args:
            input_data: Data to validate
            
        Returns:
            bool: True if valid, False otherwise
        """
        # Base validation - can be overridden by subclasses
        if not input_data:
            return False
        return True
    
    def get_task_info(self) -> Dict[str, Any]:
        """
        Get task information
        
        Returns:
            Dict containing task details
        """
        return {
            "name": self.name,
            "description": self.description,
            "agent": self.agent.get_agent_info(),
            "expected_output": self.expected_output
        }
    
    def update_description(self, new_description: str):
        """
        Update task description
        
        Args:
            new_description: New task description
        """
        self.description = new_description
        self.task.description = new_description
        self.logger.info(f"Updated task description: {new_description}")
    
    def update_expected_output(self, new_expected_output: str):
        """
        Update expected output format
        
        Args:
            new_expected_output: New expected output format
        """
        self.expected_output = new_expected_output
        self.task.expected_output = new_expected_output
        self.logger.info(f"Updated expected output: {new_expected_output}") 