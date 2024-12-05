import threading
import time
from enum import Enum, auto


class State(Enum):
    FOLLOWER = auto()
    CANDIDATE = auto()
    LEADER = auto()


class RaftNode:
    def __init__(self, id, peers):
        self.id = id
        self.peers = peers
        self.state = State.FOLLOWER
        self.current_term = 0
        self.voted_for = None
        self.log = []
        self.commit_index = 0
        self.last_applied = 0
        self.next_index = {peer: 0 for peer in peers}
        self.match_index = {peer: 0 for peer in peers}
        self.election_timeout = 10  # 10 seconds for simplicity
        self.lock = threading.Lock()
        self.leader_id = None

    def start_election(self):
        with self.lock:
            self.state = State.CANDIDATE
            self.current_term += 1
            self.voted_for = self.id
            votes = 1  # Vote for self
            threads = []
            for peer in self.peers:
                t = threading.Thread(target=self.request_vote, args=(peer,))
                threads.append(t)
                t.start()

            for t in threads:
                t.join()

            if votes > len(self.peers) / 2:
                self.state = State.LEADER
                self.leader_id = self.id
                self.replicate_log()

    def request_vote(self, peer):
        # Simulate sending request vote RPC
        # Here you should actually send the RPC and receive the vote
        time.sleep(1)  # Simulate network delay
        return True  # Assume the peer always votes for simplicity

    def replicate_log(self):
        threads = []
        for peer in self.peers:
            t = threading.Thread(target=self.send_append_entries, args=(peer,))
            threads.append(t)
            t.start()

        for t in threads:
            t.join()

    def send_append_entries(self, peer):
        # Simulate sending append entries RPC
        # Here you should actually send the RPC and handle the response
        time.sleep(1)  # Simulate network delay


# 示例初始化
node1 = RaftNode(1, [2, 3])
node2 = RaftNode(2, [1, 3])
node3 = RaftNode(3, [1, 2])

# 模拟选举和日志复制
node1.start_election()
