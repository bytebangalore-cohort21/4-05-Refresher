# Controller - The file where we build our logic
import view
import model

state = view.getuser_state()
data = model.getdata_totalseats(state)
view.showuser_data(data)


