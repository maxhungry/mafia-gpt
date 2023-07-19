from mafia.character import Bot, Player, Group
from mafia.display import ChatDisplay
import streamlit as st


class Game:
    def __init__(self, display=ChatDisplay):
        self.players = Group([
            Bot("Sally", "townspeople", avatar="💁‍♀️"),
            Bot("John", "townspeople", avatar="👱‍♂️"),
            Bot("Stan", "mafia", avatar="👨‍🦳"),
            Bot("Ottilie", "townspeople", avatar="🤠"),
            Bot("Harry", "townspeople", avatar="💂‍♂️"),
            # Player("Max")
        ])
        self.step = 0
        self.votes = {}
        self.history = []
        self.eliminated = Group([])
        self.display = display("Ducky", avatar="🦆")

    def count_votes(self, name):
        if self.votes.get(name):
            self.votes[name] += 1
        else:
            self.votes[name] = 1

    def eliminate_from_votes(self):
        print(f"Votes: {self.votes}")
        name = max(self.votes, key=self.votes.get)
        self.players.eliminate(name)
        self.votes.clear()
        self.display.show(f"{name} has been voted out 👋")

    def mafia_votes(self):
        self.display.show("Night time! Mafia please eliminate a player 🔪")

        person = self.players.random()
        print(person)
        self.players.eliminate(person.name)

        self.display.show(f"The night is over. {person.name} has been eliminated 😢")

    def game_state(self):
        m_count, t_count = self.players.count()
        if t_count == 0:
            return 'end', 'mafia'
        if m_count == 0:
            return 'end', 'townspeople'

        return 'active', None

    def start(self):
        st.session_state.clicked = False

        self.display.show("Hi, I am Ducky the mod, welcome to a new game of Mafia")

        self.mafia_votes()

        self.display.show("Let the discussion begin!")

        while True:
            match self.step:
                case 0:
                    for person in self.players:
                        reply = person.reply("", history=self.history, players=self.players)
                        self.history.append(f"{person.name}: {reply}")

                case 1:
                    for person in self.players:
                        target = person.vote(history=self.history, players=self.players)
                        self.count_votes(target)
                    self.eliminate_from_votes()

            if self.step >= 1:
                self.step = 0
                state, winner = self.game_state()
                if state == 'end':
                    self.display.show(f"Game over, {winner} win!")
                    break
            else:
                self.step += 1

        self.display.show("Bye!")
