import streamlit as st

# Initialize game state
if 'board' not in st.session_state:
    st.session_state.board = [" "] * 9  # use space instead of "-"
    st.session_state.currentplayer = "X"
    st.session_state.winner = None
    st.session_state.gamerunning = True

# Display the board with buttons
def handle_cell_click(idx):
    board = st.session_state.board
    if board[idx] == " " and st.session_state.gamerunning:
        board[idx] = st.session_state.currentplayer
        checkwin()
        checktie()
        if st.session_state.gamerunning:
            switchplayer()

def printboard():
    board = st.session_state.board
    cols = st.columns(3)
    for i in range(3):
        for j in range(3):
            idx = 3 * i + j
            label = board[idx] if board[idx] != " " else " "
            with cols[j]:
                if st.button(label, key=f"cell_{idx}"):
                    handle_cell_click(idx)

# Switch player
def switchplayer():
    st.session_state.currentplayer = "O" if st.session_state.currentplayer == "X" else "X"

# Check win conditions
def checkhorizontle():
    b = st.session_state.board
    for i in range(0, 9, 3):
        if b[i] == b[i+1] == b[i+2] != " ":
            st.session_state.winner = b[i]
            return True
    return False

def checkrow():
    b = st.session_state.board
    for i in range(3):
        if b[i] == b[i+3] == b[i+6] != " ":
            st.session_state.winner = b[i]
            return True
    return False

def checkdiag():
    b = st.session_state.board
    if b[0] == b[4] == b[8] != " ":
        st.session_state.winner = b[0]
        return True
    elif b[2] == b[4] == b[6] != " ":
        st.session_state.winner = b[2]
        return True
    return False

# Check winner
def checkwin():
    if checkhorizontle() or checkrow() or checkdiag():
        st.success(f"🎉 Winner is {st.session_state.winner}")
        st.session_state.gamerunning = False

# Check for tie
def checktie():
    if " " not in st.session_state.board and st.session_state.winner is None:
        st.info("🤝 It's a tie!")
        st.session_state.gamerunning = False

# Reset game
def reset_game():
    st.session_state.board = [" "] * 9
    st.session_state.currentplayer = "X"
    st.session_state.winner = None
    st.session_state.gamerunning = True

# --- UI Layout ---
st.title("🎮 Tic Tac Toe")
st.write(f"Current Player: `{st.session_state.currentplayer}`")
printboard()

# Restart button after game ends
if not st.session_state.gamerunning:
    if st.button("🔁 Restart Game"):
        reset_game()
