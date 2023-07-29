# Get and Save Personal API
my_API <- "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"
# Loading Required Libraries
library(stringr)
library(httr)
# Asking Questions to ChatGPT, Saving and Cleaning Answer
hey_chatGPT <- function(answer_my_question) {
  chat_GPT_answer <- POST(
    url = "https://api.openai.com/v1/chat/completions",
    add_headers(Authorization = paste("Bearer", my_API)),
    content_type_json(),
    encode = "json",
    body = list(
      model = "gpt-3.5-turbo-0301",
      messages = list(
        list(
          role = "user",
          content = answer_my_question
        )
      )
    )
  )
  str_trim(content(chat_GPT_answer)$choices[[1]]$message$content)
}

response <- hey_chatGPT("Write briefly about the history of bitcoin 
                        and ethereum?")
cat(response)




Sys.setenv(OPENAI_API_KEY = "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
")
pak::pak("MichelNivard/gptstudio")
require(devtools)
install_github("MichelNivard/gptstudio")
library(openai)
library(shiny)

library(ggplot2)
