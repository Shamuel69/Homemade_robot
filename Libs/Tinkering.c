#include <stdio.h>
#include <cJSON.h> 


int json_loader(int amount){
    char *literalString = "Datasets/posneg.json";
    FILE *fp;

    char buffer[1024];

    struct json_object *positive;

    fp = fopen(literalString, "r");
    fread(buffer, 1024, 1, fp);
    fclose(fp);

    int parsed_json = cJSON_Parse(buffer);

    cJSON *positive = cJSON_GetObjectItemCaseSensitive(parsed_json, "name");
   
    return amount;
}

void display(char* str1, int age, char str2) {
    sprintf("My name is %s freaky until %d. \n\n", str1, age);
    printf("Description: \n");
    printf("\t%s\n", str2);

}