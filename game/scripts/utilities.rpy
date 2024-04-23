init python:
    # https://blog.argentgames.co/post/2020-11-16-renpy-crossfade-music/
    renpy.music.register_channel("music2", mixer="music", loop=True, stop_on_mute=True, tight=False, file_prefix='', file_suffix='', buffer_queue=True)

    def cf(track_new, do_loop=True, curr_time=3.0, new_time=3.0):
        curr_track = "music"
        x_fade_track = "music2"
        if not renpy.music.is_playing("music"):
            x_fade_track = "music"
            curr_track = "music2"
        renpy.music.stop(curr_track,fadeout=curr_time)
        renpy.music.play(track_new,channel=x_fade_track,fadein=new_time,loop=do_loop)
        if not do_loop:
            renpy.music.queue(track_new_loop,channel=x_fade_track,loop=True)