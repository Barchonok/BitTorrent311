#
# pieces - An experimental BitTorrent client
#
# Copyright 2016 markus.eliasson@gmail.com
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import argparse
import asyncio
import os
import signal
import logging
from asyncio import Queue

from concurrent.futures import CancelledError

from pieces.protocol import PeerConnection
from pieces.torrent import Torrent
from pieces.client import TorrentClient, PieceManager
from pieces.tracker import Tracker


"""
Piece - походу это фрагмент, который отдают (ибо пошла загрузка)
Да, получен фрагмент, и мы берем новый
При have фиксировать фрагмент - уже есть в PieceManager (self.peers)

3.1Покопаться в PieceManager
4.Стратегия (часть методов уже есть, в частности rarest)
4.1 сохраняются ли данные в физ. память при загрузке торрента?

*blacklist пиров
"""
async def main():
    """parser = argparse.ArgumentParser()
    parser.add_argument('torrent',
                        help='the .torrent to download')
    parser.add_argument('-v', '--verbose', action='store_true',
                        help='enable verbose output')

    args = parser.parse_args()
    if args.verbose:
        logging.basicConfig(level=logging.INFO)"""
    logging.basicConfig(level=logging.INFO)
    #client = TorrentClient(Torrent(args.torrent))

    client = TorrentClient(Torrent('../Mytests/FB.torrent'))
    task = await asyncio.create_task(client.start())

    #await Tracker(Torrent('../Mytests/FB.torrent')).connect()
    #await Tracker(Torrent('../Mytests/FB.torrent')).connect()
    #client = TorrentClient(Torrent('../Mytests/FB.torrent'))
    #task = asyncio.create_task(client.start())
    """client = TorrentClient(Torrent('../Mytests/FB.torrent'))
    task = asyncio.create_task(client.start())

    def signal_handler(*_):
        logging.info('Exiting, please wait until everything is shutdown...')
        client.stop()
        task.cancel()

    signal.signal(signal.SIGINT, signal_handler)

    try:
        await task
    except CancelledError:
        logging.warning('Event loop was canceled')"""