from booknlp.booknlp import BookNLP

model_params={
		"pipeline":"entity,quote,supersense,event,coref", 
		"model":"small"
	}
	
booknlp=BookNLP("en", model_params)

# Input file to process
input_file="174_the_picture_of_dorian_gray_brat.txt"

# Output directory to store resulting files in
output_directory="."

# File within this directory will be named ${book_id}.entities, ${book_id}.tokens, etc.
book_id="dorian"

booknlp.process(input_file, output_directory, book_id)

# Evaluation
#TODO


#if __name__ == '__main__':
    # Evaluation
    #TODO