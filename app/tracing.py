from __future__ import annotations

import os
from functools import wraps

# --- MOCK IMPLEMENTATIONS (DEFAULT) ---
class MockContext:
    def update_trace_info(self, **kwargs): pass
    def update_current_trace(self, **kwargs): pass
    def update_current_observation(self, **kwargs): pass

def mock_observe(*args, **kwargs):
    """A mock decorator that does nothing if Langfuse is not configured."""
    def decorator(func):
        return func
    if args and callable(args[0]):
        return decorator(args[0])
    return decorator

langfuse = None
observe = mock_observe
langfuse_context = MockContext()


# --- REAL IMPLEMENTATIONS (IF CONFIGURED) ---

if (
    os.getenv("LANGFUSE_PUBLIC_KEY")
    and os.getenv("LANGFUSE_SECRET_KEY")
    and os.getenv("LANGFUSE_HOST")
):
    from langfuse import Langfuse
    from langfuse import observe as real_observe
    
    langfuse = Langfuse()
    observe = real_observe

    class LangfuseContextShim:
        """
        Lớp tương thích này "dịch" các lệnh gọi API langfuse cũ (được sử dụng
        trong bài lab) sang các lệnh gọi API mới hơn, giúp ứng dụng hoạt động
        mà không cần sửa đổi lớn.
        """
        def update_trace_info(self, **kwargs):
            self.update_current_trace(**kwargs)

        def update_current_trace(self, **kwargs):
            if hasattr(langfuse, "get_current_trace"):
                if tr := langfuse.get_current_trace():
                    tr.update(**kwargs)

        def update_current_observation(self, **kwargs):
            if hasattr(langfuse, "get_current_observation"):
                if observation := langfuse.get_current_observation():
                    usage_details = kwargs.pop("usage_details", None)
                    if usage_details:
                        try:
                            from langfuse.model import Usage
                            kwargs["usage"] = Usage(
                                input=usage_details.get("input"),
                                output=usage_details.get("output")
                            )
                        except ImportError:
                            pass
                    observation.update(**kwargs)

    langfuse_context = LangfuseContextShim()

def tracing_enabled() -> bool:
    """Check if Langfuse tracing is enabled."""
    return langfuse is not None