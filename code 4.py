# using decorator by own 

def vegeta(goku1):
    def executenow():
        print ("executing now")
        goku1()
        print ("executed")
    return executenow

@vegeta
def who_is_raghav():
    print ("raghav is the pro_gamer119")

who_is_raghav = vegeta(who_is_raghav)
who_is_raghav()

