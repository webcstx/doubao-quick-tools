"""错误定义"""


class QuickAIError(Exception):
    """基础错误"""
    pass


class AuthenticationError(QuickAIError):
    """认证错误"""
    pass


class ValidationError(QuickAIError):
    """参数校验错误"""
    pass


class RateLimitError(QuickAIError):
    """限流错误"""
    pass
