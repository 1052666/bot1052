import time
import sys
import os

# Add current directory to path so we can import local modules easily if run from outside
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from wechat_manager import WeChatManager
from ai_manager import AIManager
from processor import MessageProcessor

def main():
    print("Initializing 1052 WeChat Bot Logic with AI...")

    try:
        # 1. Initialize Transport Layer
        wx_manager = WeChatManager()
        
        # 2. Initialize AI Service
        ai_manager = AIManager()

        # 3. Initialize Logic Layer (Inject Dependencies)
        processor = MessageProcessor(wx_manager, ai_manager)

        # 4. Configuration (Isolated)
        # TODO: Add the users/groups you want to listen to here.
        # This is completely separate from the root config.py
        LISTEN_TARGETS = [
            "文件传输助手",  # Good for testing
            # "UserB",
            # "GroupC"
        ]

        # 5. Bind Listeners
        if not LISTEN_TARGETS:
            print("Warning: No listen targets configured in main.py")
        
        for target in LISTEN_TARGETS:
            wx_manager.add_listener(target, processor.handle_message)

        # 6. Main Loop
        print("Bot is running. Press Ctrl+C to stop.")
        while True:
            time.sleep(1)

    except KeyboardInterrupt:
        print("\nBot stopped by user.")
    except Exception as e:
        print(f"\nCritical Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
