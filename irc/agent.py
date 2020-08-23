# -*- coding: utf-8 -*-
# Copyright (c) 2020 HITCON Agent Contributors
# See CONTRIBUTORS file for the list of HITCON Agent Contributors

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import logging
import grpc
import kofserver_pb2, kofserver_pb2_grpc

class Agent:
    def __init__(self):
        host = Config.conf()['agentHost']
        port = Config.conf()['agentPort']

        # TODO: Check connection health
        channel = grpc.insecure_channel('%s:%d'%(host, port))
        logging.info("Agent Connecting...")
        f = grpc.channel_ready_future(channel)
        try:
            f.result(timeout=Config.conf()['agentConnectTimeout'])
            logging.info("Agent Connected")
        except Exception:
            # Failed to connect.
            return False

        # The gRPC channel
        self.channel = channel
        # The kofserver gRPC stub
        self.stub = kofserver_pb2_grpc.KOFServerStub(self.channel)

    def shellcode(game_name, player_name, shellcode):
        response = self.stub.PlayerIssueSC(kofserver_pb2.PlayerIssueSC(gameName=game_name, playerName=player_name, shellcode=shellcode))
        if response.error == kofserver_pb2.ErrorCode.ERROR_NONE:
            print("shellcode successful")
        else:
            print("shellcode failed: %s"%(str(response.error),))
    
    # TODO: CreateGame
    # TODO: StartGame
    # TODO: DestroyGame