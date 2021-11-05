from LinkedList import LinkedList

class Queue:
    def __init__(self):
        self.list = LinkedList()
        self.length = 0

    def __len__(self):
        return self.length

    def __str__(self):
        values = []
        node = self.list.head
        while node:
            values.append(str(node))
            node = node.next
        values.reverse()
        return " -> ".join(values)

    def enqueue(self, value):
        self.length += 1
        self.list.add(value)

    def dequeue(self):
        if self.length == 0:
            return None
        self.length -= 1
        popped = self.list.head.value
        self.list.head = self.list.head.next
        return popped

class AnimalShelter:
    def __init__(self):
        self.cats = Queue()
        self.dogs = Queue()

    def enqueue(self, animal_type, animal):
        if animal_type == 'Cat':
            self.cats.enqueue(animal)
        elif animal_type == 'Dog':
            self.dogs.enqueue(animal)
    
    def dequeueCat(self):
        return self.cats.dequeue()

    def dequeueDog(self):
        return self.dogs.dequeue()

    def dequeueAny(self):
        if len(self.cats) > len(self.dogs):
            return self.cats.dequeue()
        else:
            return self.dogs.dequeue()

if __name__ == '__main__':
    shelter = AnimalShelter()
    shelter.enqueue('Cat', 'First Cat')
    shelter.enqueue('Cat', 'Second Cat')
    shelter.enqueue('Dog', 'First Dog')
    shelter.enqueue('Cat', 'Another Cat')
    shelter.enqueue('Dog', 'Second Dog')
    print(shelter.dequeueCat())
    print(shelter.dequeueAny())
    print(shelter.dequeueAny())
    print(shelter.dequeueDog())
        