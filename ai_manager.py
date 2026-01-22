import time
try:
    from openai import OpenAI
except ImportError:
    print("Please install openai library: pip install openai")
    raise

import config

class AIManager:
    def __init__(self):
        """Initialize the OpenAI client using configuration."""
        try:
            self.client = OpenAI(
                api_key=config.API_KEY,
                base_url=config.BASE_URL
            )
            self.model = config.MODEL_NAME
            self.system_prompt = config.SYSTEM_PROMPT
            print(f"AI Manager initialized. Model: {self.model}")
        except Exception as e:
            print(f"Failed to initialize AI Manager: {e}")
            self.client = None

    def get_response(self, user_input, history=[]):
        """
        Get response from AI model.
        
        Args:
            user_input: The current user message.
            history: List of previous messages [{"role": "user", "content": "..."}, ...]
        
        Returns:
            str: The AI's response text.
        """
        if not self.client:
            return "AI Service is not available (Initialization failed)."
        
        # 1. Construct messages list
        messages = [{"role": "system", "content": self.system_prompt}]
        
        # Add history
        if history:
            messages.extend(history)
            
        # Add current user input
        messages.append({"role": "user", "content": user_input})

        try:
            # 2. Call API
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                stream=False
            )
            
            # 3. Extract content
            content = response.choices[0].message.content
            
            # Simple cleaning (e.g. remove <think> tags if using DeepSeek R1)
            if "<think>" in content:
                content = content.split("</think>")[-1].strip()
                
            return content

        except Exception as e:
            print(f"AI API Error: {e}")
            return f"Error getting response: {str(e)}"
