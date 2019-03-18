class computer(object):
    def __init__(self, ram, motherboard, gpu):
        self.processor = True
        self.motherboard = motherboard
        self.gpu = gpu
        self.storage = ram
        self.storageleft = 100

    def run(self, storageused):
        if self.processor:
            if self.storageleft <= 0:
                print("You've ran out of storage.")
            else:
                storage_total = self.storageleft - storageused
                print("You have %s storage left." % storage_total)

    def gpu(self, gpu):
        if self.gpu:
            if self.gpu =




kyle_computer = computer(False, True, False)

kyle_computer.run(100)


