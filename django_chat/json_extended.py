import json


class ExtendedJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        # obj가 set 타입일 경우
        if isinstance(obj, set):
            # 다음과 같은 dict로 변환후 리턴
            return {"__set__": True, "values": tuple(obj)}


class ExtendedJSONDecoder(json.JSONDecoder):
    def __init__(self, **kwargs):
        # keyword arguments 에 다음과 같은 값 삽입
        kwargs.setdefault('object_hook', self._object_hook)
        #상속 받겠다는 의미
        super().__init__(**kwargs)
    
    # 전역 메소드
    @staticmethod
    def _object_hook(dct):
        # 딕셔너리를 set으로 변환후 반환
        if '__set__' in dct:
            return set(dct['values'])
        return dct
