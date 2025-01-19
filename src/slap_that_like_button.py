import enum


class LikeState(enum.Enum):
    empty = enum.auto()
    liked = enum.auto()
    disliked = enum.auto()


slap_like_transitions = {
    LikeState.empty: LikeState.liked,
    LikeState.liked: LikeState.empty,
    LikeState.disliked: LikeState.liked,
}

slap_dislike_transitions = {
    LikeState.empty: LikeState.disliked,
    LikeState.liked: LikeState.disliked,
    LikeState.disliked: LikeState.empty,
}


def slap_like(state: LikeState) -> LikeState:
    return slap_like_transitions[state]


def slap_dislike(state: LikeState) -> LikeState:
    return slap_dislike_transitions[state]


def slaps_many(state: LikeState, slaps: str) -> LikeState:
    for slap in slaps:
        slap = slap.lower()
        if slap == "l":
            state = slap_like(state)
        elif slap == "d":
            state = slap_dislike(state)
        else:
            raise ValueError("invalid slap")
    return state


def main():
    example = LikeState
    print(example.empty)
    print(example.empty.name)
    print(example.empty.value)
    print(example.liked.value)
    print(type(example.empty))


if __name__ == "__main__":
    main()
