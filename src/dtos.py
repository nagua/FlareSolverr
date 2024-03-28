from typing import Optional

STATUS_OK = "ok"
STATUS_ERROR = "error"


class ChallengeResolutionResultT:
    url: Optional[str] = None
    status: Optional[int] = None
    headers: Optional[list] = None
    response: Optional[str] = None
    cookies: Optional[list] = None
    userAgent: Optional[str] = None

    def __init__(self, _dict):
        self.__dict__.update(_dict)


class ChallengeResolutionT:
    status: Optional[str] = None
    message: Optional[str] = None
    result: Optional[ChallengeResolutionResultT] = None

    def __init__(self, _dict):
        self.__dict__.update(_dict)
        if self.result is not None:
            self.result = ChallengeResolutionResultT(self.result)


class V1RequestBase(object):
    # V1RequestBase
    cmd: Optional[str] = None
    cookies: Optional[list] = None
    maxTimeout: Optional[int] = None
    proxy: Optional[dict] = None
    session: Optional[str] = None
    session_ttl_minutes: Optional[int] = None
    headers: Optional[list] = None  # deprecated v2.0.0, not used
    userAgent: Optional[str] = None  # deprecated v2.0.0, not used

    # V1Request
    url: Optional[str] = None
    postData: Optional[str] = None
    returnOnlyCookies: Optional[bool] = None
    download: Optional[bool] = None   # deprecated v2.0.0, not used
    returnRawHtml: Optional[bool] = None  # deprecated v2.0.0, not used

    # Additional
    shortWaitTimeout: Optional[int] = None

    def __init__(self, _dict):
        self.__dict__.update(_dict)


class V1ResponseBase(object):
    # V1ResponseBase
    status: Optional[str] = None
    message: Optional[str] = None
    session: Optional[str] = None
    sessions: Optional[list[str]] = None
    startTimestamp: Optional[int] = None
    endTimestamp: Optional[int] = None
    version: Optional[str] = None

    # V1ResponseSolution
    solution: Optional[ChallengeResolutionResultT] = None

    # hidden vars
    __error_500__: bool = False

    def __init__(self, _dict):
        self.__dict__.update(_dict)
        if self.solution is not None:
            self.solution = ChallengeResolutionResultT(self.solution)


class IndexResponse(object):
    msg: Optional[str] = None
    version: Optional[str] = None
    userAgent: Optional[str] = None

    def __init__(self, _dict):
        self.__dict__.update(_dict)


class HealthResponse(object):
    status: Optional[str] = None

    def __init__(self, _dict):
        self.__dict__.update(_dict)
