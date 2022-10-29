{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMXeWUuQI11QPBzsBQ8U6en",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Wata-Naoki/atcoder/blob/main/ABC129A.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "input_list=list(map(int, input().split()))\n",
        "\n",
        "input_list.sort()\n",
        "print(sum(input_list[:2]))\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ymu1Jj0UKIoU",
        "outputId": "9d769045-3b35-4cff-9a7b-d8b320b3f523"
      },
      "execution_count": 15,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "1 3 4\n",
            "4\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 14,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "OyL0BGvV1hzz",
        "outputId": "38da797b-70d8-4ff9-fbb2-1ee9c82f3aba"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "1 1 1\n",
            "1\n"
          ]
        }
      ],
      "source": [
        "input_list=list(map(int, input().split()))\n",
        "# print(input_list)\n",
        "\n",
        "ans_list=[]\n",
        "# print(\"---------------------------\")\n",
        "\n",
        "for i, v in enumerate(input_list):\n",
        "  # print(i)\n",
        "  for k in input_list:\n",
        "    if input_list[i] is k:\n",
        "      # ans=input_list[i]+k\n",
        "      # ans_list.append(ans)\n",
        "      # print(input_list[i], k)\n",
        "      continue\n",
        "    else:\n",
        "       ans=input_list[i]+k\n",
        "       ans_list.append(ans)\n",
        "try:\n",
        "  print(min(ans_list))\n",
        "except:\n",
        "    print(input_list[0])\n",
        "\n",
        "\n",
        "\n"
      ]
    }
  ]
}