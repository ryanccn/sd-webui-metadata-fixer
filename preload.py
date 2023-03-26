def preload(parser):
    parser.add_argument(
        "--metadata-prefix", type=str, help="Prefix to metadata text", default=None
    )
    parser.add_argument(
        "--metadata-suffix", type=str, help="Suffix to metadata text", default=None
    )
