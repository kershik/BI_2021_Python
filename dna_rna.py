from abc import ABC, abstractmethod

class Sequence(ABC):
    
    @abstractmethod
    def gc_content(self):
        pass
    
    @abstractmethod
    def reverse_complement(self):
        pass

    
class Dna(Sequence):
    
    def __init__(self, sequence):
        self.sequence = sequence.upper()
        
    def gc_content(self):
        gc_count = self.sequence.count('G') + self.sequence.count('C')
        return gc_count / len(self.sequence)
    
    def reverse_complement(self):
        # creates new atribute complement
        trans_table = str.maketrans({
            'A': 'T',
            'T': 'A',
            'G': 'C',
            'C': 'G'
        })
        self.complement = self.sequence.translate(trans_table)
        return self
    
    def transcribe(self):
        transcribe_table = str.maketrans({
            'A': 'U',
            'T': 'A',
            'G': 'C',
            'C': 'G'
        })
        return(Rna(self.sequence.translate(transcribe_table)))
    
    def __iter__(self):
        self.current = -1
        return self
    
    def __next__(self):
        if self.current == len(self.sequence) - 1:
            raise StopIteration
        self.current += 1
        return self.sequence[self.current]
    
    def __eq__(self, other):
        if not isinstance(other, Dna):
            return NotImplemented
        return self.sequence == other.sequence
    
    def __hash__(self):
        return hash(self.sequence)
    
    
class Rna(Sequence):
    
    def __init__(self, sequence):
        self.sequence = sequence.upper()
        
    def gc_content(self):
        gc_count = self.sequence.count('G') + self.sequence.count('C')
        return gc_count / len(self.sequence)
    
    def reverse_complement(self):
        # creates new atribute complement 
        trans_table = str.maketrans({
            'A': 'U',
            'U': 'A',
            'G': 'C',
            'C': 'G'
        })
        self.complement = self.sequence.translate(trans_table)
        return self
    
    def __iter__(self):
        self.current = -1
        return self
    
    def __next__(self):
        if self.current == len(self.sequence) - 1:
            raise StopIteration
        self.current += 1
        return self.sequence[self.current]
    
    def __eq__(self, other):
        if not isinstance(other, Rna):
            return NotImplemented
        return self.sequence == other.sequence
    
    def __hash__(self):
        return hash(self.sequence)
    
    