
import React, { useState } from 'react';
import { Header, SectionHeader } from '../components/Header';
import { ContentPanel } from '../components/ContentPanel';
import { QUIZ_QUESTIONS } from '../constants';
import { UserAnswers } from '../types';

export const QuizPage: React.FC = () => {
  const [answers, setAnswers] = useState<UserAnswers>({});
  const [submitted, setSubmitted] = useState(false);
  const [score, setScore] = useState(0);

  const handleOptionChange = (questionId: string, option: string) => {
    setAnswers(prev => ({ ...prev, [questionId]: option }));
  };

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    let currentScore = 0;
    QUIZ_QUESTIONS.forEach(q => {
      if (answers[q.id] === q.correctAnswer) {
        currentScore++;
      }
    });
    setScore(currentScore);
    setSubmitted(true);
  };
  
  const totalQuestions = QUIZ_QUESTIONS.length;
  const percentage = totalQuestions > 0 ? score / totalQuestions : 0;
  
  const getResultUI = () => {
      if (percentage === 1) {
          return <div className="p-4 bg-green-900/50 border border-green-400 text-green-300 rounded-lg">🎉 <strong>VALIDACIÓ COMPLETA! Codi 100% Acceptat!</strong> 🎉</div>
      } else if (percentage >= 0.7) {
          return <div className="p-4 bg-yellow-900/50 border border-yellow-400 text-yellow-300 rounded-lg">VALIDACIÓ PARCIALMENT OK. Repassa els punts febles.</div>
      } else {
          return <div className="p-4 bg-red-900/50 border border-red-400 text-red-300 rounded-lg">ERROR CRÍTIC. Repassa la UF1 abans de tornar a executar el test.</div>
      }
  }

  return (
    <div>
      <Header icon="❓" title="Posa't a Prova!" subtitle="Terminal de Test - NF 1.1, 1.2, 1.3" />
      <div className="p-4 rounded-lg bg-blue-900/20 border border-blue-400/30 text-blue-300 mb-6">
        🟢 <strong>EXECUTANT TEST DE VALIDACIÓ DE CONEIXEMENTS...</strong> Aquesta prova cobreix totes les unitats formatives.
      </div>

      {!submitted ? (
        <form onSubmit={handleSubmit}>
          <ContentPanel className="space-y-6">
            {QUIZ_QUESTIONS.map(q => (
              <div key={q.id} className="border-b border-gray-700 pb-6 last:border-b-0 last:pb-0">
                <p className="font-bold text-gray-400 text-sm mb-1">{q.title}</p>
                <p className="text-white mb-3">{q.question}</p>
                <div role="radiogroup" className="flex flex-col sm:flex-row sm:flex-wrap gap-2">
                  {q.options.map(option => (
                    <label key={option} className={`block w-full sm:w-auto px-4 py-2 rounded-md border-2 transition-all duration-200 cursor-pointer ${answers[q.id] === option ? 'bg-[#00CCCC] text-[#0A0A0A] border-[#00FFFF]' : 'bg-[#0A0A0A] border-gray-600 hover:border-[#00CCCC]'}`}>
                      <input
                        type="radio"
                        name={q.id}
                        value={option}
                        checked={answers[q.id] === option}
                        onChange={() => handleOptionChange(q.id, option)}
                        className="sr-only"
                      />
                      <span>{option}</span>
                    </label>
                  ))}
                </div>
              </div>
            ))}
             <button type="submit" className="w-full mt-6 py-3 px-6 bg-[#00FFFF] text-black font-bold rounded-lg hover:bg-white [box-shadow:0_0_10px_#00FFFF] transition-all duration-300">
                ⏩ INICIAR ESCANEIG DE RESULTATS (ENVIAR) 🚀
            </button>
          </ContentPanel>
        </form>
      ) : (
        <ContentPanel>
          <SectionHeader title="✅ INFORME DE VALIDACIÓ FINAL:" className="mt-0" />
          <div className="space-y-4 mb-6">
            {QUIZ_QUESTIONS.map(q => {
              const userAnswer = answers[q.id];
              const isCorrect = userAnswer === q.correctAnswer;
              return (
                <div key={q.id} className={`p-3 rounded-md border ${isCorrect ? 'bg-green-900/20 border-green-700' : 'bg-red-900/20 border-red-700'}`}>
                  <p className="font-bold text-gray-300">{q.title}</p>
                  <div className="flex items-start gap-3 mt-2">
                    <span className={`text-xl font-bold ${isCorrect ? 'text-green-400' : 'text-red-400'}`}>{isCorrect ? '✓' : '✗'}</span>
                    <div>
                      <p className="text-sm text-gray-400">La teva resposta: <code className="bg-gray-700 px-1 rounded">{userAnswer || 'No contestada'}</code></p>
                      {!isCorrect && <p className="text-sm text-green-400 mt-1">Correcta: <code className="bg-green-900/50 px-1 rounded">{q.correctAnswer}</code></p>}
                    </div>
                  </div>
                </div>
              );
            })}
          </div>
          <hr className="border-gray-700 my-6" />
          <h3 className="text-2xl font-bold text-white mb-2">Puntuació Final del Sistema: {score}/{totalQuestions}</h3>
          <div className="w-full bg-gray-700 rounded-full h-4 border border-[#00CCCC] p-0.5">
            <div className="bg-gradient-to-r from-[#00FFFF] to-[#00CCCC] h-full rounded-full transition-all duration-500" style={{ width: `${percentage * 100}%` }}></div>
          </div>
          <div className="mt-6">
            {getResultUI()}
          </div>
           <button onClick={() => { setSubmitted(false); setAnswers({}); setScore(0); }} className="w-full mt-6 py-3 px-6 bg-gray-600 text-white font-bold rounded-lg hover:bg-gray-500 transition-all duration-300">
                ↻ TORNAR A INTENTAR
            </button>
        </ContentPanel>
      )}
    </div>
  );
};
