from __future__ import absolute_import
from .Interface import Interface
from .CuePoint import CuePoint
from .Scene import Scene
from .Track import Track


class Song(Interface):
    def __init__(self, c_instance, socket):
        super(Song, self).__init__(c_instance, socket)
        self.song = self.ableton.song()

    def get_ns(self, nsid):
        return self.song

    def create_audio_track(self, ns, index):
        return Track.serialize_track(ns.create_audio_track(index))

    def create_midi_track(self, ns, index):
        return Track.serialize_track(ns.create_midi_track(index))

    def create_return_track(self, ns):
        return Track.serialize_track(ns.create_return_track())

    def get_clip_trigger_quantization(self, ns):
        return str(ns.clip_trigger_quantization)

    def get_cue_points(self, ns):
        sorted_points = sorted(ns.cue_points, key=lambda cue: cue.time)
        return list(map(CuePoint.serialize_cue_point, sorted_points))

    def get_master_track(self, ns):
        return Track.serialize_track(ns.master_track)

    def get_midi_recording_quantization(self, ns):
        return str(ns.midi_recording_quantization)

    def get_return_tracks(self, ns):
        return list(map(Track.serialize_track, ns.return_tracks))

    def get_scenes(self, ns):
        return list(map(Scene.serialize_scene, ns.scenes))

    def get_tracks(self, ns):
        return list(map(Track.serialize_track, ns.tracks))

    def get_visible_tracks(self, ns):
        return list(map(Track.serialize_track, ns.visible_tracks))

    def get_data(self, ns, key):
        return ns.get_data(key, None)

    def get_current_smpte_song_time(self, ns, timeFormat):
        time = ns.get_current_smpte_song_time(timeFormat)
        return {'hours': time.hours, 'minutes': time.minutes, 'seconds': time.seconds, 'frames': time.frames}
