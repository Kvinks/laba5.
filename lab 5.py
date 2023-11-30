class Candidate:
    
    def __init__(self, name):
        self.name = name
        self.votes = 0
        
    def add_votes(self, num_votes):
        self.votes += num_votes
        
    def calculate_percentage(self, total_votes):
        if total_votes > 0:
            return (self.votes / total_votes) * 100
        else:
            return 0


class Elections:
    
    def __init__(self):
        self.candidates = []

    def add_candidate(self, candidate):
        self.candidates.append(candidate)
    
    def calculate_winner(self):
        winner = max(self.candidates, key=lambda candidate: candidate.votes)
        return winner


def main():
    election = Elections()

    for i in range(5):
        name = input(f"Введіть прізвище кандидата {i + 1}: ")
        candidate = Candidate(name)
        election.add_candidate(candidate)

    total_votes = 0

    for candidate in election.candidates:
        num_votes = int(input(f"Введіть кількість голосів для кандидата {candidate.name}: "))
        candidate.add_votes(num_votes)
        total_votes += num_votes

    print("\nРезультати виборів:")
    
    for candidate in election.candidates:
        print(f"{candidate.name}: {candidate.votes} голосів, {candidate.calculate_percentage(total_votes):.2f}%")

    winner = election.calculate_winner()

    if winner:
        print(f"\nПереможець виборів: {winner.name}")

if __name__ == "__main__":
    main()