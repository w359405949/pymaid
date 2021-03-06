import time
import gevent

from pymaid.channel import Channel
from pymaid.agent import ServiceAgent
from pymaid.utils import ProfilerContext
from heartbeat_pb2 import LongPlaying_Stub


def main():
    channel = Channel()
    conn = channel.connect("127.0.0.1", 8888, ignore_heartbeat=True)
    service = ServiceAgent(LongPlaying_Stub(channel), conn)

    resp = service.over_two_seconds()
    assert resp
    time.sleep(4)
    # switch greenlet so conn can close
    gevent.sleep(0.1)
    assert conn.is_closed, conn.is_closed

if __name__ == "__main__":
    with ProfilerContext():
        main()
