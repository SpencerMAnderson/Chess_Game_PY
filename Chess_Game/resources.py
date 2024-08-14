from init import init_images
#from utils import tint_pieces

def load_images():
    wp, bp, wkn, bkn, wb, bb, wr, br, wq, bq, wk, bk = init_images()
    piece_images = {
        'wp': wp,
        'bp': bp,
        'wkn': wkn,
        'bkn': bkn,
        'wb': wb,
        'bb': bb,
        'wr': wr,
        'br': br,
        'wq': wq,
        'bq': bq,
        'wk': wk,
        'bk': bk
    }
    return piece_images
piece_images = load_images()

# Names of pieces
pieces = {
    'wp': "White Pawn",
    'bp': "Black Pawn",
    'wkn': "White Knight",
    'bkn': "Black Knight",
    'wb': "White Bishop",
    'bb': "Black Bishop",
    'wr': "White Rook",
    'br': "Black Rook",
    'wq': "White Queen",
    'bq': "Black Queen",
    'wk': "White King",
    'bk': "Black King"
}
