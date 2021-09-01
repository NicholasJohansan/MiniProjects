# default lib imports
from os import system
from sys import exit
from time import sleep
from gc import collect as gc_collect
# others
from asyncio import run as async_run
from winrt.windows.media.control import GlobalSystemMediaTransportControlsSessionManager, GlobalSystemMediaTransportControlsSession
import pypresence
MediaManager = GlobalSystemMediaTransportControlsSessionManager

class Application:
	""" Main Application Class """
	GROOVE_SESSION_ID = "Microsoft.ZuneMusic_8wekyb3d8bbwe!Microsoft.ZuneMusic"
	DRP_ID = 853607917168361512
	REFRESH_DELAY = 1
	convert_to_dict = lambda obj: {attr: obj.__getattribute__(attr) for attr in dir(obj) if attr[0] != "_"}
	version = "1.0.0"

	def __init__(self):
		self.data = {}
		self.start()

	def start(self):
		print(
f"""
Groove Music DRP v{self.version}
[0] - Start Automatic [Unstable]
[1] - Start Manual
[2] - Exit
Select an option
>> 
"""
)
		option = input()
		system('cls')
		if option not in ["0", "1", "2"]:
			print("Invalid option, try again!\n")
			self.start()
		elif option == "0" or option == "1":
			self.automatic = True if option == "0" else False
			self.RPC = pypresence.Presence(self.DRP_ID, pipe=0)
			self.RPC.connect()
			print(self.RPC.update())
			self.main_process()
		elif option == "2":
			exit()
		
	def main_process(self):
		""" method for main process """
		system('cls')
		try:
			if self.automatic:
				while True:
					try:
						data = self.fetch_info()
						if data == self.data:
							del data
							gc_collect()
							continue
						gc_collect()
					except IndexError:
						data = {"playback_status": "Idle"}
					self.update_status(data)
					del data
					gc_collect()
					sleep(self.REFRESH_DELAY)
					gc_collect()
			else:
				while True:
					try:
						data = self.fetch_info()
					except IndexError:
						data = {"playback_status": "Idle"}
					self.update_status(data)
					input("\nenter to update status")

		except KeyboardInterrupt:
			return

	def update_status(self, data):
		if data != self.data:
			self.data = data
			system('cls')
			if self.data["playback_status"] != "Idle":
				print(f"Song Details:\n   [Title] {self.data['song_title']}\n[Duration] {self.data['song_duration']}\n  [Status] {self.data['playback_status']}")
				self.RPC.update(
					large_image="groove_music",
					large_text=f"Groove Music DRP v{self.version}",
					small_image=("play" if self.data['playback_status'] == "Playing" else "pause"),
					small_text=self.data['playback_status'],
					details=self.data['song_title'],
					state=f"Duration: {self.data['song_duration']//60}min {self.data['song_duration']%60}s"
				)
			else:
				print(f"Groove Music is not opened")
				self.RPC.update(
					large_image="groove_music",
					large_text=f"Groove Music DRP v{self.version}",
					small_image="pause",
					small_text="Idle",
					details="No Song Selected",
					state=f"Idle"
				)
		del data
		gc_collect()

	async def get_session(self):
		sessions = await MediaManager.request_async()
		return list(filter(
			lambda session: session.source_app_user_model_id == self.GROOVE_SESSION_ID,
			sessions.get_sessions()
		))[0]

	async def get_song_title(self, session):
		info = await session.try_get_media_properties_async()
		return info.title

	def fetch_info(self):
		session = async_run(self.get_session())

		data = {}
		data["song_title"] = async_run(self.get_song_title(session))
		data["song_duration"] = round((session.get_timeline_properties().end_time.duration)/10**7)
		data["playback_status"] = "Paused" if session.get_playback_info().playback_status == 5 else "Playing" 
		#print(f"Current Media Info:{current_media_info}")
		#
		#print(f"Playback Info: {playback_info}")
		#controls_info = self.__class__.convert_to_dict(playback_info['controls'])
		#print(f"Playback Controls Info: {controls_info}")
		#
		#position_info = self.__class__.convert_to_dict(timeline_info['position'])
		#print(f"Position Info: {position_info}")
		del session
		gc_collect()
		return data

if __name__ == "__main__":
	Application()