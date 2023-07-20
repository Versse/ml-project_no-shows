from metaflow import FlowSpec, step, card


class NoShows(FlowSpec):
    """_summary_

    Args:
        FlowSpec (_type_): _description_
    """
    
    @card
    @step
    def start(self):
        """_summary_ls
        """
        print('no shows is starting')    
        self.next(self.end)
    
    @card
    @step
    def end(self):
        """_summary_
        """
        print('no shows is ending')
        
if __name__ == "__main__":
    NoShows()