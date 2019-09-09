export interface Bundle {
  id: number;
  is_bonus: boolean;
  is_published: Boolean;
  quiz_for_EY: {
    [key: string]: Quiz
  };
  quiz_for_SY: {
    [key: string]: Quiz
  };
}

export interface Quiz {
  answer: string;
  id: number;
  question_image: string;
  question: string;
  source_link: string;
  status: string;
  title: string;
}
