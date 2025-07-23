import streamlit as st
import random
import matplotlib.pyplot as plt
import matplotlib

# 日本語フォントの設定（Windows向け）
matplotlib.rcParams['font.family'] = 'MS Gothic'

def generate_amidakuji(vertical_lines, horizontal_lines):
    connections = []
    for _ in range(horizontal_lines):
        pos = random.randint(0, vertical_lines - 2)
        connections.append(pos)
    return connections

def traverse_amidakuji(start, connections, vertical_lines):
    position = start
    for conn in connections:
        if position == conn:
            position += 1
        elif position == conn + 1:
            position -= 1
    return position

def simulate_amidakuji(vertical_lines, horizontal_lines, goal_index, trials):
    hit_counts = [0] * vertical_lines
    for _ in range(trials):
        connections = generate_amidakuji(vertical_lines, horizontal_lines)
        for start in range(vertical_lines):
            end = traverse_amidakuji(start, connections, vertical_lines)
            if end == goal_index:
                hit_counts[start] += 1
    return hit_counts

# Streamlit UI
st.title("あみだくじシミュレーション")

vertical_lines = st.slider("縦線の本数", 2, 20, 8)
horizontal_lines = st.slider("横線の本数", 0, 50, 12)
goal_index = st.number_input("当たりの位置（左から0番目）", min_value=0, max_value=vertical_lines-1, value=3)
trials = st.number_input("試行回数", min_value=1, max_value=10000, value=1000)

if st.button("シミュレーション開始"):
    results = simulate_amidakuji(vertical_lines, horizontal_lines, goal_index, trials)
    fig, ax = plt.subplots()
    ax.bar(range(vertical_lines), results, tick_label=[f"{i+1}" for i in range(vertical_lines)])
    ax.set_xlabel("vertical line")
    ax.set_ylabel("probabilty")
    ax.set_title(f"win position：{goal_index+1}（trial：{trials}）")
    st.pyplot(fig)
