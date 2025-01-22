from src.slap_that_like_button import LikeState, slaps_many


def test_slaps():
    assert slaps_many(LikeState.empty, "") is LikeState.empty
    assert slaps_many(LikeState.empty, "l") is LikeState.liked
    assert slaps_many(LikeState.empty, "d") is LikeState.disliked
    assert slaps_many(LikeState.empty, "ll") is LikeState.empty
    assert slaps_many(LikeState.empty, "dd") is LikeState.empty
    assert slaps_many(LikeState.empty, "ld") is LikeState.disliked
    assert slaps_many(LikeState.empty, "dl") is LikeState.liked
    assert slaps_many(LikeState.empty, "ldd") is LikeState.empty
    assert slaps_many(LikeState.empty, "lldd") is LikeState.empty
    assert slaps_many(LikeState.empty, "ddl") is LikeState.liked
    assert slaps_many(LikeState.empty, "ddll") is LikeState.empty
